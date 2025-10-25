"""
Function implementations for Azure OpenAI function calling
These functions are called when the LLM decides to retrieve dynamic data
"""

import json
from mock_data import (
    mock_new_hires_db, 
    mock_onboarding_tasks, 
    get_employee_by_name,
    get_urgent_tasks,
    update_task_status_in_db
)


def get_employee_info(employee_identifier):
    """
    Get information about an employee by ID or name
    
    Args:
        employee_identifier: Employee ID (e.g., "E123") or name (e.g., "Nguyen Van An")
    
    Returns:
        dict: Employee information or error message
    """
    # Try as employee ID first
    if employee_identifier in mock_new_hires_db:
        return {
            "success": True,
            "data": mock_new_hires_db[employee_identifier]
        }
    
    # Try as name
    employee = get_employee_by_name(employee_identifier)
    if employee:
        return {
            "success": True,
            "data": employee
        }
    
    return {
        "success": False,
        "error": f"Không tìm thấy nhân viên với ID hoặc tên: {employee_identifier}"
    }


def get_onboarding_tasks(employee_identifier, status_filter=None):
    """
    Get onboarding tasks for an employee
    
    Args:
        employee_identifier: Employee ID (e.g., "E123") or name
        status_filter: Optional filter by status ("Pending", "Done", or None for all)
    
    Returns:
        dict: List of tasks or error message
    """
    # Get employee ID
    employee_id = employee_identifier
    if employee_identifier not in mock_new_hires_db:
        employee = get_employee_by_name(employee_identifier)
        if employee:
            employee_id = employee["employee_id"]
        else:
            return {
                "success": False,
                "error": f"Không tìm thấy nhân viên với ID hoặc tên: {employee_identifier}"
            }
    
    # Get tasks
    if employee_id not in mock_onboarding_tasks:
        return {
            "success": False,
            "error": f"Không tìm thấy nhiệm vụ cho nhân viên {employee_id}"
        }
    
    tasks = mock_onboarding_tasks[employee_id]
    
    # Filter by status if requested
    if status_filter:
        tasks = [task for task in tasks if task["status"].lower() == status_filter.lower()]
    
    return {
        "success": True,
        "employee_id": employee_id,
        "data": tasks,
        "total_tasks": len(tasks)
    }


def update_task_status(task_id, new_status):
    """
    Update the status of an onboarding task
    
    Args:
        task_id: Task ID (e.g., "T01")
        new_status: New status ("Done" or "Pending")
    
    Returns:
        dict: Update result with task information
    """
    result = update_task_status_in_db(task_id, new_status)
    return result


def send_introduction_message(employee_identifier, recipient_type):
    """
    Mock function to send introduction message to buddy or manager
    
    Args:
        employee_identifier: Employee ID or name
        recipient_type: "buddy" or "manager"
    
    Returns:
        dict: Mock result of sending introduction
    """
    # Get employee info
    if employee_identifier in mock_new_hires_db:
        employee = mock_new_hires_db[employee_identifier]
    else:
        employee = get_employee_by_name(employee_identifier)
        if not employee:
            return {
                "success": False,
                "error": f"Không tìm thấy nhân viên: {employee_identifier}"
            }
    
    if recipient_type.lower() == "buddy":
        recipient_name = employee["buddy"]
        recipient_email = employee["buddy_email"]
        recipient_teams = employee["buddy_teams"]
    elif recipient_type.lower() == "manager":
        recipient_name = employee["manager"]
        recipient_email = employee["manager_email"]
        recipient_teams = employee["manager_teams"]
    else:
        return {
            "success": False,
            "error": "recipient_type phải là 'buddy' hoặc 'manager'"
        }
    
    # Mock sending message
    return {
        "success": True,
        "message": f"Đã gửi lời giới thiệu đến {recipient_name}",
        "recipient": {
            "name": recipient_name,
            "email": recipient_email,
            "teams_link": recipient_teams
        },
        "employee_name": employee["name"]
    }


def check_urgent_tasks(employee_identifier):
    """
    Check for urgent tasks that are due soon
    
    Args:
        employee_identifier: Employee ID or name
    
    Returns:
        dict: List of urgent tasks with days left
    """
    # Get employee ID
    employee_id = employee_identifier
    if employee_identifier not in mock_new_hires_db:
        employee = get_employee_by_name(employee_identifier)
        if employee:
            employee_id = employee["employee_id"]
        else:
            return {
                "success": False,
                "error": f"Không tìm thấy nhân viên: {employee_identifier}"
            }
    
    urgent_tasks = get_urgent_tasks(employee_id, days_threshold=2)
    
    return {
        "success": True,
        "employee_id": employee_id,
        "urgent_tasks": urgent_tasks,
        "count": len(urgent_tasks)
    }


# Function schemas for Azure OpenAI
# These tell the LLM what functions are available and how to call them
FUNCTION_DEFINITIONS = [
    {
        "name": "get_employee_info",
        "description": "Lấy thông tin chi tiết về một nhân viên mới, bao gồm tên, email, quản lý, buddy, phòng ban, và ngày bắt đầu làm việc. Sử dụng khi người dùng hỏi về thông tin cá nhân, quản lý, buddy, hoặc chi tiết nhân viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_identifier": {
                    "type": "string",
                    "description": "Mã nhân viên (ví dụ: 'E123') hoặc tên nhân viên (ví dụ: 'Nguyen Van An'). Nếu người dùng nói 'tôi' hoặc 'của tôi', hãy sử dụng mã nhân viên mặc định 'E123'."
                }
            },
            "required": ["employee_identifier"]
        }
    },
    {
        "name": "get_onboarding_tasks",
        "description": "Lấy danh sách các nhiệm vụ onboarding của một nhân viên mới, bao gồm mô tả, hạn chót, trạng thái, và độ ưu tiên. Sử dụng khi người dùng hỏi về nhiệm vụ, công việc cần làm, hoặc lịch trình onboarding.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_identifier": {
                    "type": "string",
                    "description": "Mã nhân viên (ví dụ: 'E123') hoặc tên nhân viên. Nếu người dùng nói 'tôi' hoặc 'của tôi', hãy sử dụng mã nhân viên mặc định 'E123'."
                },
                "status_filter": {
                    "type": "string",
                    "enum": ["Pending", "Done"],
                    "description": "Lọc nhiệm vụ theo trạng thái. Để trống để lấy tất cả nhiệm vụ."
                }
            },
            "required": ["employee_identifier"]
        }
    },
    {
        "name": "update_task_status",
        "description": "Cập nhật trạng thái của một nhiệm vụ onboarding. Sử dụng khi người dùng thông báo đã hoàn thành một nhiệm vụ hoặc muốn thay đổi trạng thái nhiệm vụ.",
        "parameters": {
            "type": "object",
            "properties": {
                "task_id": {
                    "type": "string",
                    "description": "Mã nhiệm vụ (ví dụ: 'T01', 'T02'). Trích xuất từ danh sách nhiệm vụ đã hiển thị trước đó."
                },
                "new_status": {
                    "type": "string",
                    "enum": ["Done", "Pending"],
                    "description": "Trạng thái mới của nhiệm vụ. 'Done' nếu hoàn thành, 'Pending' nếu chưa hoàn thành."
                }
            },
            "required": ["task_id", "new_status"]
        }
    },
    {
        "name": "send_introduction_message",
        "description": "Gửi tin nhắn giới thiệu đến buddy hoặc manager qua email/Teams. Sử dụng khi người dùng muốn kết nối với buddy hoặc manager của họ.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_identifier": {
                    "type": "string",
                    "description": "Mã nhân viên hoặc tên nhân viên. Nếu người dùng nói 'tôi', sử dụng 'E123'."
                },
                "recipient_type": {
                    "type": "string",
                    "enum": ["buddy", "manager"],
                    "description": "Người nhận tin nhắn: 'buddy' hoặc 'manager'."
                }
            },
            "required": ["employee_identifier", "recipient_type"]
        }
    },
    {
        "name": "check_urgent_tasks",
        "description": "Kiểm tra các nhiệm vụ sắp đến hạn (trong vòng 2 ngày). Sử dụng để nhắc nhở chủ động về deadline.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_identifier": {
                    "type": "string",
                    "description": "Mã nhân viên hoặc tên nhân viên. Nếu người dùng nói 'tôi', sử dụng 'E123'."
                }
            },
            "required": ["employee_identifier"]
        }
    }
]


def execute_function(function_name, arguments):
    """
    Execute a function by name with given arguments
    
    Args:
        function_name: Name of the function to execute
        arguments: JSON string or dict of function arguments
    
    Returns:
        dict: Function result
    """
    # Parse arguments if string
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except json.JSONDecodeError:
            return {
                "success": False,
                "error": "Invalid arguments format"
            }
    
    # Execute the appropriate function
    if function_name == "get_employee_info":
        return get_employee_info(arguments.get("employee_identifier"))
    elif function_name == "get_onboarding_tasks":
        return get_onboarding_tasks(
            arguments.get("employee_identifier"),
            arguments.get("status_filter")
        )
    elif function_name == "update_task_status":
        return update_task_status(
            arguments.get("task_id"),
            arguments.get("new_status")
        )
    elif function_name == "send_introduction_message":
        return send_introduction_message(
            arguments.get("employee_identifier"),
            arguments.get("recipient_type")
        )
    elif function_name == "check_urgent_tasks":
        return check_urgent_tasks(arguments.get("employee_identifier"))
    else:
        return {
            "success": False,
            "error": f"Unknown function: {function_name}"
        }

