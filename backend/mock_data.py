"""
Mock data for Employee Onboarding Chatbot
Contains FAQs, employee information, and onboarding tasks
"""

# Mock data for FAQ (Used for System Prompt / Few-Shot)
onboarding_faqs = [
    {
        "q": "Khi nào tôi nhận lương?",
        "a": "Lương thử việc được trả vào ngày 15 của tháng tiếp theo. Lương chính thức sẽ được trả vào ngày 10 hàng tháng."
    },
    {
        "q": "Làm sao để cài đặt email công ty?",
        "a": "Bạn vui lòng truy cập IT Portal tại http://it.fpt.com để xem hướng dẫn chi tiết. Bộ phận IT sẽ gửi thông tin đăng nhập qua email cá nhân của bạn trong ngày đầu tiên."
    },
    {
        "q": "Chính sách nghỉ phép như thế nào?",
        "a": "Trong thời gian thử việc, bạn chưa có ngày phép. Sau khi lên chính thức, bạn sẽ có 12 ngày phép/năm, được tính theo tháng làm việc."
    },
    {
        "q": "Ai là người hỗ trợ tôi trong thời gian onboarding?",
        "a": "Bạn sẽ có một Buddy (người đồng hành) được chỉ định để hỗ trợ trong 3 tháng đầu. Thông tin Buddy của bạn có trong hệ thống."
    },
    {
        "q": "Giờ làm việc của công ty là gì?",
        "a": "Giờ làm việc tiêu chuẩn là 8:30 - 17:30 từ thứ 2 đến thứ 6, với 1 giờ nghỉ trưa. Một số dự án có thể có giờ làm việc linh hoạt."
    },
    {
        "q": "Tôi cần hoàn thành những khóa học bắt buộc nào?",
        "a": "Tất cả nhân viên mới phải hoàn thành: Security Awareness Training, Code of Conduct, và Company Orientation trong 2 tuần đầu tiên."
    }
]

# Mock data for new hire employees (Used for Function Calling)
mock_new_hires_db = {
    "E123": {
        "employee_id": "E123",
        "name": "Nguyễn Văn An",
        "email": "an.nguyen@fsoft.com.vn",
        "phone": "+84 98 765 4321",
        "manager": "Lê Thị Bình",
        "manager_email": "binh.le@fsoft.com.vn",
        "manager_phone": "+84 91 234 5678",
        "manager_teams": "https://teams.microsoft.com/l/chat/binh.le",
        "buddy": "Trần Văn Cường",
        "buddy_email": "cuong.tran@fsoft.com.vn",
        "buddy_phone": "+84 93 456 7890",
        "buddy_teams": "https://teams.microsoft.com/l/chat/cuong.tran",
        "department": "Software Development",
        "start_date": "2025-10-20",
        "position": "Software Engineer"
    },
    "E456": {
        "employee_id": "E456",
        "name": "Đặng Phú Quý",
        "email": "quy.dang@fsoft.com.vn",
        "phone": "+84 97 654 3210",
        "manager": "Phạm Văn Dũng",
        "manager_email": "dung.pham@fsoft.com.vn",
        "manager_phone": "+84 92 345 6789",
        "manager_teams": "https://teams.microsoft.com/l/chat/dung.pham",
        "buddy": "Vũ Thị Em",
        "buddy_email": "em.vu@fsoft.com.vn",
        "buddy_phone": "+84 94 567 8901",
        "buddy_teams": "https://teams.microsoft.com/l/chat/em.vu",
        "department": "Quality Assurance",
        "start_date": "2025-10-21",
        "position": "QA Engineer"
    },
    "E789": {
        "employee_id": "E789",
        "name": "Hoàng Thị Giang",
        "email": "giang.hoang@fsoft.com.vn",
        "phone": "+84 96 543 2109",
        "manager": "Ngô Văn Hùng",
        "manager_email": "hung.ngo@fsoft.com.vn",
        "manager_phone": "+84 90 123 4567",
        "manager_teams": "https://teams.microsoft.com/l/chat/hung.ngo",
        "buddy": "Đỗ Thị Lan",
        "buddy_email": "lan.do@fsoft.com.vn",
        "buddy_phone": "+84 95 678 9012",
        "buddy_teams": "https://teams.microsoft.com/l/chat/lan.do",
        "department": "Business Analysis",
        "start_date": "2025-10-22",
        "position": "Business Analyst"
    }
}

# Mock data for onboarding tasks (Used for Function Calling)
mock_onboarding_tasks = {
    "E123": [
        {
            "task_id": "T01",
            "task": "Hoàn thành khóa học Security Awareness",
            "description": "Truy cập Learning Portal và hoàn thành khóa học về bảo mật thông tin",
            "due_date": "2025-10-25",
            "status": "Pending",
            "priority": "High"
        },
        {
            "task_id": "T02",
            "task": "Gặp mặt Buddy",
            "description": "Gặp gỡ và làm quen với Buddy được chỉ định",
            "due_date": "2025-10-22",
            "status": "Done",
            "priority": "High"
        },
        {
            "task_id": "T03",
            "task": "Thiết lập môi trường dev",
            "description": "Cài đặt các công cụ: VS Code, Git, Docker theo hướng dẫn",
            "due_date": "2025-10-27",
            "status": "Pending",
            "priority": "Medium"
        },
        {
            "task_id": "T04",
            "task": "Đọc tài liệu dự án",
            "description": "Đọc và nắm bắt tài liệu kỹ thuật của dự án được phân công",
            "due_date": "2025-10-30",
            "status": "Pending",
            "priority": "Medium"
        },
        {
            "task_id": "T05",
            "task": "Hoàn thành Code of Conduct training",
            "description": "Học và ký xác nhận đã hiểu quy tắc ứng xử của công ty",
            "due_date": "2025-10-26",
            "status": "Pending",
            "priority": "High"
        }
    ],
    "E456": [
        {
            "task_id": "T06",
            "task": "Hoàn thành khóa học Security Awareness",
            "description": "Truy cập Learning Portal và hoàn thành khóa học về bảo mật thông tin",
            "due_date": "2025-10-26",
            "status": "Pending",
            "priority": "High"
        },
        {
            "task_id": "T07",
            "task": "Đọc tài liệu dự án ABC",
            "description": "Nắm bắt quy trình testing và tài liệu test cases của dự án ABC",
            "due_date": "2025-10-30",
            "status": "Pending",
            "priority": "Medium"
        },
        {
            "task_id": "T08",
            "task": "Thiết lập môi trường test",
            "description": "Cài đặt Selenium, Postman, và các công cụ testing khác",
            "due_date": "2025-10-28",
            "status": "Pending",
            "priority": "High"
        },
        {
            "task_id": "T09",
            "task": "Gặp mặt Buddy",
            "description": "Gặp gỡ và làm quen với Buddy được chỉ định",
            "due_date": "2025-10-23",
            "status": "Done",
            "priority": "High"
        }
    ],
    "E789": [
        {
            "task_id": "T10",
            "task": "Hoàn thành khóa học Security Awareness",
            "description": "Truy cập Learning Portal và hoàn thành khóa học về bảo mật thông tin",
            "due_date": "2025-10-27",
            "status": "Pending",
            "priority": "High"
        },
        {
            "task_id": "T11",
            "task": "Học về quy trình Agile",
            "description": "Tham gia workshop về Scrum và quy trình làm việc Agile",
            "due_date": "2025-10-29",
            "status": "Pending",
            "priority": "Medium"
        },
        {
            "task_id": "T12",
            "task": "Gặp mặt team và stakeholders",
            "description": "Tham gia meeting giới thiệu với team và các stakeholders chính",
            "due_date": "2025-10-24",
            "status": "Pending",
            "priority": "High"
        }
    ]
}


def get_all_employee_ids():
    """Get list of all employee IDs in the system"""
    return list(mock_new_hires_db.keys())


def get_employee_by_name(name):
    """Find employee by name (case-insensitive partial match)"""
    name_lower = name.lower()
    for emp_id, emp_data in mock_new_hires_db.items():
        if name_lower in emp_data["name"].lower():
            return emp_data
    return None


def get_urgent_tasks(employee_id, days_threshold=2):
    """
    Get tasks that are due soon (within threshold days)
    Used for proactive reminders
    """
    from datetime import datetime, timedelta
    
    if employee_id not in mock_onboarding_tasks:
        return []
    
    today = datetime.now()
    threshold_date = today + timedelta(days=days_threshold)
    
    urgent_tasks = []
    for task in mock_onboarding_tasks[employee_id]:
        if task["status"] == "Pending":
            try:
                due_date = datetime.strptime(task["due_date"], "%Y-%m-%d")
                if today <= due_date <= threshold_date:
                    days_left = (due_date - today).days
                    task_with_urgency = task.copy()
                    task_with_urgency["days_left"] = days_left
                    urgent_tasks.append(task_with_urgency)
            except ValueError:
                continue
    
    return urgent_tasks


def update_task_status_in_db(task_id, new_status):
    """
    Update task status in mock database
    Returns success status and updated task info
    """
    for employee_id, tasks in mock_onboarding_tasks.items():
        for task in tasks:
            if task["task_id"] == task_id:
                old_status = task["status"]
                task["status"] = new_status
                return {
                    "success": True,
                    "employee_id": employee_id,
                    "task": task,
                    "old_status": old_status
                }
    
    return {
        "success": False,
        "error": f"Không tìm thấy nhiệm vụ với ID: {task_id}"
    }

