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
        "team_name": "Cloud Warriors",
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
        "team_name": "Monorepo Avengers",
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
        "team_name": "Agile Ninjas",
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


# Mock data for teams (Used for team meetings and collaboration)
mock_team_db = {
    "Cloud Warriors": {
        "team_name": "Cloud Warriors",
        "lead": "Lê Thị Bình",
        "lead_email": "binh.le@fsoft.com.vn",
        "members_count": 8,
        "meetings": [
            {
                "name": "Daily Standup",
                "schedule": "9:00 AM mỗi ngày (T2-T6)",
                "duration": "15 phút",
                "link": "https://teams.microsoft.com/l/meetup/cloud-warriors-daily",
                "type": "recurring"
            },
            {
                "name": "Sprint Planning",
                "schedule": "2:00 PM mỗi thứ 2 (2 tuần/lần)",
                "duration": "2 giờ",
                "link": "https://teams.microsoft.com/l/meetup/cloud-warriors-sprint",
                "type": "recurring"
            },
            {
                "name": "Tech Sharing Session",
                "schedule": "4:00 PM thứ 5 hàng tuần",
                "duration": "1 giờ",
                "link": "https://teams.microsoft.com/l/meetup/cloud-warriors-tech",
                "type": "recurring"
            }
        ]
    },
    "Monorepo Avengers": {
        "team_name": "Monorepo Avengers",
        "lead": "Phạm Văn Dũng",
        "lead_email": "dung.pham@fsoft.com.vn",
        "members_count": 12,
        "meetings": [
            {
                "name": "Team Daily Standup",
                "schedule": "9:00 AM mỗi ngày (T2-T6)",
                "duration": "15 phút",
                "link": "https://teams.microsoft.com/l/meetup/monorepo-daily",
                "type": "recurring"
            },
            {
                "name": "Project ABC Sync-up",
                "schedule": "3:00 PM mỗi thứ 6",
                "duration": "1 giờ",
                "link": "https://teams.microsoft.com/l/meetup/monorepo-syncup",
                "type": "recurring"
            },
            {
                "name": "QA Review Meeting",
                "schedule": "10:00 AM mỗi thứ 3",
                "duration": "1.5 giờ",
                "link": "https://teams.microsoft.com/l/meetup/monorepo-qa",
                "type": "recurring"
            }
        ]
    },
    "Agile Ninjas": {
        "team_name": "Agile Ninjas",
        "lead": "Ngô Văn Hùng",
        "lead_email": "hung.ngo@fsoft.com.vn",
        "members_count": 6,
        "meetings": [
            {
                "name": "Daily Standup",
                "schedule": "9:15 AM mỗi ngày (T2-T6)",
                "duration": "15 phút",
                "link": "https://teams.microsoft.com/l/meetup/agile-ninjas-daily",
                "type": "recurring"
            },
            {
                "name": "Backlog Refinement",
                "schedule": "2:00 PM mỗi thứ 4",
                "duration": "1 giờ",
                "link": "https://teams.microsoft.com/l/meetup/agile-ninjas-backlog",
                "type": "recurring"
            },
            {
                "name": "Sprint Retrospective",
                "schedule": "4:00 PM thứ 6 (2 tuần/lần)",
                "duration": "1 giờ",
                "link": "https://teams.microsoft.com/l/meetup/agile-ninjas-retro",
                "type": "recurring"
            }
        ]
    }
}

# Mock knowledge base for IT/HR support (Used in System Prompt)
mock_knowledge_base = {
    "it_support": [
        {
            "topic": "WiFi F-town 3",
            "network": "FPT_Guest",
            "password": "FtownGuest@2025",
            "contact": "it-hcm@fpt.com",
            "phone": "028-7300-8866 (ext. 101)"
        },
        {
            "topic": "WiFi F-town 2",
            "network": "FPT_Guest",
            "password": "FtownGuest@2024",
            "contact": "it-hcm@fpt.com",
            "phone": "028-7300-8866 (ext. 101)"
        },
        {
            "topic": "VPN Access",
            "guide": "http://it.fpt.com/vpn-guide",
            "software": "FortiClient VPN",
            "contact": "it-support@fpt.com"
        },
        {
            "topic": "Email Setup",
            "guide": "http://it.fpt.com/email-setup",
            "system": "Outlook 365",
            "contact": "it-support@fpt.com"
        },
        {
            "topic": "Laptop/Hardware Issues",
            "contact": "it-hcm@fpt.com",
            "phone": "028-7300-8866 (ext. 101)",
            "location": "IT Counter - Tầng 1 F-town 3"
        }
    ],
    "hr_systems": [
        {
            "name": "Nghỉ phép",
            "system": "F-Leave",
            "link": "http://fleave.fpt.com",
            "description": "Đăng ký nghỉ phép, nghỉ bù, nghỉ không lương",
            "approval": "Quản lý trực tiếp phê duyệt"
        },
        {
            "name": "Chấm công",
            "system": "F-Timesheet",
            "link": "http://ftimesheet.fpt.com",
            "description": "Nhập giờ làm việc, overtime",
            "deadline": "Hàng tháng trước ngày 25"
        },
        {
            "name": "Phiếu lương",
            "system": "F-Pay",
            "link": "http://fpay.fpt.com",
            "description": "Xem phiếu lương, lịch sử thu nhập",
            "availability": "Phiếu lương có vào ngày 5 hàng tháng"
        },
        {
            "name": "Đào tạo nội bộ",
            "system": "F-Learning",
            "link": "http://flearning.fpt.com",
            "description": "Các khóa học bắt buộc và tự chọn",
            "contact": "learning@fpt.com"
        }
    ],
    "office_info": [
        {
            "location": "F-town 3",
            "address": "Lô T2-6, Đường D1, Khu Công nghệ cao, Q.9, TP.HCM",
            "working_hours": "8:30 AM - 5:30 PM (T2-T6)",
            "parking": "Miễn phí cho xe máy và ô tô",
            "canteen": "Tầng 1 và Tầng 8"
        },
        {
            "location": "F-town 2",
            "address": "Lô T2-3, Đường D1, Khu Công nghệ cao, Q.9, TP.HCM",
            "working_hours": "8:30 AM - 5:30 PM (T2-T6)",
            "parking": "Miễn phí cho xe máy",
            "canteen": "Tầng 1"
        }
    ]
}

# ============================================================================
# HR POLICY & KNOWLEDGE BASE (Extended)
# ============================================================================

# Mock HR Policy Database - Used for System Prompt
mock_hr_policy = {
    "compensation": {
        "pay_date": "Lương được trả vào ngày 28 hàng tháng. Nếu ngày 28 là cuối tuần, bạn sẽ nhận vào thứ 6 trước đó.",
        "pay_slip_components": "Phiếu lương (payslip) bao gồm: Lương cơ bản (Gross), các khoản phụ cấp (nếu có), các khoản giảm trừ (Thuế TNCN, Bảo hiểm), và Lương thực nhận (Net).",
        "ot_policy": "Lương OT được tính: 150% vào ngày thường, 200% vào cuối tuần, 300% vào ngày lễ. OT phải được quản lý duyệt trước trên hệ thống F-Timesheet.",
        "thang_13": "Lương tháng 13 được trả cùng lương tháng 12, tỷ lệ dựa trên số tháng làm việc chính thức trong năm.",
        "probation_salary": "Lương thử việc = 85% lương chính thức. Sau khi vượt qua thử việc, bạn sẽ nhận đủ 100% lương và các phúc lợi đầy đủ."
    },
    "benefits": {
        "health_insurance": "Bạn có 1 tháng (kể từ ngày ký hợp đồng chính thức) để đăng ký bảo hiểm sức khỏe cho người thân. Vui lòng truy cập Hệ thống F-Benefits (http://fbenefits.fpt.com) để đăng ký.",
        "wellness_allowance": "Công ty hỗ trợ 500.000 VND/tháng cho chi phí điện thoại (đối với level Senior trở lên) và có liên kết giảm giá với các phòng tập gym (California, CityGym).",
        "annual_health_check": "Nhân viên được khám sức khỏe định kỳ 1 lần/năm tại các bệnh viện liên kết (Vinmec, FV Hospital). Thông báo sẽ được gửi qua email.",
        "meal_allowance": "Phụ cấp ăn trưa: 730.000 VND/tháng (đối với văn phòng không có canteen miễn phí)."
    },
    "leave_policy": {
        "how_to_apply": "Tất cả các loại nghỉ phép (phép năm, nghỉ ốm, nghỉ không lương...) đều phải được tạo yêu cầu trên Hệ thống F-Leave (http://fleave.fpt.com) và được quản lý trực tiếp duyệt.",
        "annual_leave": "Nhân viên mới được 12 ngày phép năm. Sau mỗi năm làm việc, số ngày phép tăng thêm 1 ngày (tối đa 18 ngày).",
        "sick_leave": "Nghỉ ốm từ 2 ngày liên tiếp trở lên cần có giấy xác nhận của bệnh viện/bác sĩ. Nghỉ ốm 1 ngày không cần giấy nhưng phải thông báo quản lý.",
        "special_leave": "Bạn được nghỉ 3 ngày (có lương) cho kết hôn, và 3 ngày (có lương) cho tang chế (cha/mẹ/vợ/chồng/con). Cần nộp giấy tờ cho HR.",
        "unpaid_leave": "Nghỉ không lương cần đăng ký trước ít nhất 1 tuần và được quản lý + HR duyệt.",
        "carry_forward": "Phép năm không sử dụng hết có thể chuyển sang năm sau (tối đa 5 ngày) hoặc quy đổi thành tiền (theo chính sách công ty)."
    },
    "career": {
        "levels": "Lộ trình phát triển kỹ thuật (Engineer) gồm: L1 (Junior) -> L2 (Senior) -> L3 (Lead) -> L4 (Architect). Mỗi level có yêu cầu kỹ năng và kinh nghiệm riêng.",
        "review_cycle": "Công ty có 2 kỳ đánh giá hiệu suất (Performance Review) lớn vào Tháng 6 (Giữa năm) và Tháng 12 (Cuối năm). Kết quả review ảnh hưởng đến tăng lương và thăng tiến.",
        "goal_setting": "Việc thiết lập mục tiêu (Goals) được thực hiện trên Hệ thống F-Goals (http://fgoals.fpt.com) vào đầu mỗi kỳ (Tháng 1 và Tháng 7).",
        "promotion": "Thăng tiến dựa trên: Hiệu suất công việc, Kỹ năng chuyên môn, Đóng góp cho team/dự án, và Thời gian ở level hiện tại (tối thiểu 1 năm).",
        "training_budget": "Mỗi nhân viên có ngân sách đào tạo 10 triệu VND/năm cho các khóa học bên ngoài (Udemy, Coursera, Conference...)."
    },
    "internal_systems": {
        "F-Pay": "Xem phiếu lương hàng tháng, lịch sử thu nhập, và chứng từ thuế TNCN tại http://fpay.fpt.com",
        "F-Timesheet": "Chấm công (check-in/out), đăng ký OT, và xem báo cáo giờ làm tại http://ftimesheet.fpt.com",
        "F-Leave": "Đăng ký nghỉ phép, xem số dư phép, và lịch sử nghỉ phép tại http://fleave.fpt.com",
        "F-Expense": "Thanh toán chi phí (công tác, tiếp khách, đào tạo) tại http://fexpense.fpt.com. Cần đính kèm hóa đơn/chứng từ.",
        "F-Benefits": "Đăng ký bảo hiểm sức khỏe, xem phúc lợi, và quản lý thông tin người thân tại http://fbenefits.fpt.com",
        "F-Goals": "Thiết lập và theo dõi mục tiêu công việc (OKR/KPI) tại http://fgoals.fpt.com",
        "IT-Request": "Đăng ký mua/đổi thiết bị (laptop, chuột, bàn phím, màn hình) tại http://itrequest.fpt.com. Yêu cầu cần được quản lý duyệt.",
        "F-Learning": "Truy cập thư viện khóa học nội bộ và đăng ký đào tạo tại http://flearning.fpt.com"
    },
    "expense_policy": {
        "business_trip": "Chi phí công tác (đi lại, khách sạn, ăn uống) được hoàn trả 100% theo định mức. Đăng ký trước chuyến đi trên F-Expense.",
        "client_entertainment": "Chi phí tiếp khách (ăn uống, quà tặng) cần có sự phê duyệt của quản lý trước khi phát sinh.",
        "training_expense": "Chi phí đào tạo (khóa học, sách, conference) được hoàn trả trong hạn mức 10 triệu/năm. Cần nộp chứng chỉ/chứng nhận sau khóa học.",
        "equipment": "Thiết bị làm việc (laptop, màn hình) do công ty cấp. Thiết bị cá nhân (chuột, bàn phím, tai nghe) được hỗ trợ tối đa 2 triệu VND/năm."
    }
}

# Mock Leave Balance Database - Used for Function Calling
mock_leave_db = {
    "E123": {
        "employee_id": "E123",
        "annual_leave_total": 12,
        "annual_leave_used": 3.5,
        "annual_leave_remaining": 8.5,
        "sick_leave_total": 12,
        "sick_leave_used": 0,
        "sick_leave_remaining": 12,
        "unpaid_leave_used": 0,
        "special_leave_used": 0
    },
    "E456": {
        "employee_id": "E456",
        "annual_leave_total": 13,
        "annual_leave_used": 1.0,
        "annual_leave_remaining": 12.0,
        "sick_leave_total": 12,
        "sick_leave_used": 2,
        "sick_leave_remaining": 10,
        "unpaid_leave_used": 0,
        "special_leave_used": 0
    },
    "E789": {
        "employee_id": "E789",
        "annual_leave_total": 12,
        "annual_leave_used": 5.0,
        "annual_leave_remaining": 7.0,
        "sick_leave_total": 12,
        "sick_leave_used": 1,
        "sick_leave_remaining": 11,
        "unpaid_leave_used": 0,
        "special_leave_used": 3  # Used for wedding
    }
}

# Mock Training Courses Database - Used for Function Calling
mock_training_db = [
    {
        "id": "C001",
        "name": "Advanced React 18 and Next.js",
        "type": "Technical",
        "category": "Frontend Development",
        "platform": "Udemy Business",
        "duration": "40 hours",
        "level": "Advanced",
        "link": "http://flearning.fpt.com/course/C001"
    },
    {
        "id": "C002",
        "name": "Monorepo Development with Nx",
        "type": "Technical",
        "category": "Software Architecture",
        "platform": "Internal Workshop",
        "duration": "16 hours",
        "level": "Intermediate",
        "link": "http://flearning.fpt.com/course/C002"
    },
    {
        "id": "C003",
        "name": "Effective Communication for Engineers",
        "type": "Soft Skill",
        "category": "Communication",
        "platform": "Coursera",
        "duration": "20 hours",
        "level": "All Levels",
        "link": "http://flearning.fpt.com/course/C003"
    },
    {
        "id": "C004",
        "name": "Generative AI Fundamentals",
        "type": "Technical",
        "category": "AI/ML",
        "platform": "Internal Workshop",
        "duration": "24 hours",
        "level": "Beginner",
        "link": "http://flearning.fpt.com/course/C004"
    },
    {
        "id": "C005",
        "name": "Azure Cloud Architecture",
        "type": "Technical",
        "category": "Cloud Computing",
        "platform": "Microsoft Learn",
        "duration": "30 hours",
        "level": "Intermediate",
        "link": "http://flearning.fpt.com/course/C005"
    },
    {
        "id": "C006",
        "name": "Leadership Skills for Tech Leads",
        "type": "Soft Skill",
        "category": "Leadership",
        "platform": "Internal Workshop",
        "duration": "12 hours",
        "level": "Advanced",
        "link": "http://flearning.fpt.com/course/C006"
    },
    {
        "id": "C007",
        "name": "Python for Data Analysis",
        "type": "Technical",
        "category": "Data Science",
        "platform": "Udemy Business",
        "duration": "35 hours",
        "level": "Intermediate",
        "link": "http://flearning.fpt.com/course/C007"
    },
    {
        "id": "C008",
        "name": "Agile & Scrum Fundamentals",
        "type": "Soft Skill",
        "category": "Project Management",
        "platform": "Coursera",
        "duration": "15 hours",
        "level": "Beginner",
        "link": "http://flearning.fpt.com/course/C008"
    }
]


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


def find_task_by_name(employee_id, task_name_keyword):
    """
    Find task by partial name match for confirmation
    Used in interactive task update workflow
    """
    if employee_id not in mock_onboarding_tasks:
        return None
    
    task_name_lower = task_name_keyword.lower()
    for task in mock_onboarding_tasks[employee_id]:
        if task_name_lower in task["task"].lower():
            return task
    
    return None


def get_leave_balance_from_db(employee_id):
    """
    Get leave balance for an employee
    Returns leave balance data or None if not found
    """
    return mock_leave_db.get(employee_id)


def search_training_courses_in_db(keyword=None, course_type=None):
    """
    Search training courses by keyword or type
    Returns list of matching courses
    """
    results = []
    
    if not keyword and not course_type:
        # Return all courses if no filter
        return mock_training_db
    
    keyword_lower = keyword.lower() if keyword else ""
    
    for course in mock_training_db:
        match = False
        
        # Search by keyword in name, category
        if keyword:
            if (keyword_lower in course["name"].lower() or 
                keyword_lower in course["category"].lower()):
                match = True
        
        # Filter by type
        if course_type:
            if course["type"].lower() == course_type.lower():
                match = True if not keyword else (match and True)
        
        if match or (not keyword and not course_type):
            results.append(course)
    
    return results

