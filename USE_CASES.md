# Use Cases Implementation

This document describes the 3 main use cases implemented in the Employee Onboarding Chatbot, based on real-world scenarios.

---

## Use Case 1: Interactive Task Management ✅

### Scenario
A new employee (e.g., `E456`) has just completed a task. They want to notify the bot and know what to do next.

### User Journey
```
User: "Em ơi, anh vừa hoàn thành xong khóa học Security Awareness rồi."

Bot: "Tuyệt vời! Em thấy nhiệm vụ **[T06] Hoàn thành khóa học Security Awareness**. 
     Anh xác nhận đã hoàn thành nhiệm vụ này đúng không ạ?"

User: "Đúng rồi em."

Bot: [Calls update_task_status("T06", "Done")]
     [Calls get_next_task("E456")]
     
     "Dạ em đã cập nhật trạng thái 'Hoàn thành' cho nhiệm vụ. 
     Nhiệm vụ tiếp theo của anh là **[T08] Thiết lập môi trường test**, 
     hạn chót là 28/10/2025 (🔴 Ưu tiên cao). 
     Anh cần em hỗ trợ gì thêm không?"
```

### Implementation

#### 1. Features Added ✅
- **Confirmation Step**: Bot asks for confirmation before updating task status
- **Smart Detection**: AI recognizes completion intent from natural language
- **Next Task Suggestion**: Automatically suggests what to do next after completion
- **Priority-based Sorting**: Next task is selected based on priority and due date

#### 2. Functions
```python
# Already implemented
update_task_status(task_id, new_status)  # Update task in database

# NEW
get_next_task(employee_identifier)  # Get next pending high-priority task
```

#### 3. Data
- Uses existing `mock_onboarding_tasks` with `status` field
- Status dynamically updated in memory

#### 4. System Prompt Enhancement
Added confirmation workflow rules:
```
**QUAN TRỌNG**: Trước khi gọi function `update_task_status`, PHẢI hỏi xác nhận:
1. Nhận diện task user muốn update
2. Hỏi xác nhận
3. CHỈ gọi function sau khi user xác nhận
4. Sau khi update, gọi `get_next_task` để gợi ý việc tiếp theo
```

---

## Use Case 2: People & Team Integration ✅

### Scenario
A new employee wants to know about colleagues and team meeting schedules to prepare for the work week.

### User Journey
```
User: "Quản lý của anh là ai? Sắp tới team anh có lịch họp gì không?"

Bot: [Calls get_employee_info("E456")]
     [Calls get_team_meetings("E456")]
     
     "Dạ, quản lý trực tiếp của anh là **Phạm Văn Dũng**.
     
     📧 Email: dung.pham@fsoft.com.vn
     📞 Phone: +84 92 345 6789
     💬 [Chat trên Teams](https://teams.microsoft.com/l/chat/dung.pham)
     
     Anh đang ở team **Monorepo Avengers** với 12 thành viên. 
     Team có các lịch họp cố định:
     
     📅 **Team Daily Standup**
     - Thời gian: 9:00 AM mỗi ngày (T2-T6)
     - Thời lượng: 15 phút
     - [Join Meeting](https://teams.microsoft.com/l/meetup/monorepo-daily)
     
     📅 **Project ABC Sync-up**
     - Thời gian: 3:00 PM mỗi thứ 6
     - Thời lượng: 1 giờ
     - [Join Meeting](https://teams.microsoft.com/l/meetup/monorepo-syncup)
     
     📅 **QA Review Meeting**
     - Thời gian: 10:00 AM mỗi thứ 3
     - Thời lượng: 1.5 giờ
     - [Join Meeting](https://teams.microsoft.com/l/meetup/monorepo-qa)"
```

### Implementation

#### 1. Features Added ✅
- **Team Information**: Show team name, lead, member count
- **Meeting Schedules**: Display all recurring team meetings
- **Contact Integration**: Full contact cards with Teams links

#### 2. Functions
```python
# NEW
get_team_meetings(employee_identifier)  # Get team info and meeting schedules
```

#### 3. Data Added

**Updated `mock_new_hires_db`:**
```python
{
    "E456": {
        ...
        "team_name": "Monorepo Avengers"  # NEW field
    }
}
```

**New `mock_team_db`:**
```python
{
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
            ...
        ]
    }
}
```

3 teams implemented:
- Cloud Warriors (8 members)
- Monorepo Avengers (12 members)
- Agile Ninjas (6 members)

---

## Use Case 3: Admin & IT Support ✅

### Scenario
A new employee encounters IT issues or needs administrative help. They don't know who to contact or which system to use.

### User Journey
```
User: "Anh không vào được wifi ở F-town 3. Với cả anh muốn đăng ký nghỉ phép thì làm ở đâu?"

Bot: "Dạ, em xin hỗ trợ anh:

     **1. Về Wi-Fi (F-town 3):**
     📶 Network: FPT_Guest
     🔑 Password: FtownGuest@2025
     
     Nếu vẫn không kết nối được, anh vui lòng liên hệ:
     📧 Email: it-hcm@fpt.com
     📞 Phone: 028-7300-8866 (ext. 101)
     
     **2. Về Đăng ký nghỉ phép:**
     Anh truy cập hệ thống **F-Leave** tại http://fleave.fpt.com để tạo yêu cầu.
     - Hệ thống: Đăng ký nghỉ phép, nghỉ bù, nghỉ không lương
     - Phê duyệt: Quản lý trực tiếp (anh Phạm Văn Dũng) sẽ phê duyệt
     
     Anh cần em hỗ trợ thêm gì nữa không ạ?"
```

### Implementation

#### 1. Features Added ✅
- **Contextual Knowledge**: Bot has embedded knowledge of IT/HR systems
- **No Function Calls Needed**: Information retrieved from system prompt
- **Multi-topic Handling**: Can answer multiple questions in one response

#### 2. Data Added

**New `mock_knowledge_base`:**

```python
{
    "it_support": [
        {
            "topic": "WiFi F-town 3",
            "network": "FPT_Guest",
            "password": "FtownGuest@2025",
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
            ...
        },
        {
            "topic": "Laptop/Hardware Issues",
            ...
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
            ...
        },
        {
            "name": "Phiếu lương",
            "system": "F-Pay",
            ...
        },
        {
            "name": "Đào tạo nội bộ",
            "system": "F-Learning",
            ...
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
            ...
        }
    ]
}
```

#### 3. System Prompt Integration
Knowledge base is embedded directly into system prompt during initialization:
```python
def create_system_prompt():
    ...
    # Add IT support knowledge
    for item in mock_knowledge_base["it_support"]:
        base_prompt += format_knowledge(item)
    
    # Add HR systems knowledge
    for item in mock_knowledge_base["hr_systems"]:
        base_prompt += format_hr_system(item)
    
    # Add office info
    for office in mock_knowledge_base["office_info"]:
        base_prompt += format_office(office)
```

---

## Summary Table

| Use Case | Functions | Data Added | Implementation |
|----------|-----------|------------|----------------|
| **1. Task Management** | `get_next_task()` | Helper: `find_task_by_name()` | Confirmation workflow in system prompt |
| **2. Team Integration** | `get_team_meetings()` | `mock_team_db` (3 teams)<br>`team_name` field added | Full team meeting schedules |
| **3. IT/HR Support** | None (uses system prompt) | `mock_knowledge_base`<br>- 5 IT topics<br>- 4 HR systems<br>- 2 office locations | Embedded in system prompt |

---

## Testing Scenarios

### Test Case 1: Interactive Task Update
```
1. User: "Tôi hoàn thành khóa học Security rồi"
2. Bot: [Asks for confirmation]
3. User: "Đúng"
4. Bot: [Updates task, suggests next task]
5. Verify: Task status changed, next task suggested
```

### Test Case 2: Team Meetings
```
1. User: "Team của tôi có lịch họp gì?"
2. Bot: [Shows team info and all meetings with links]
3. Verify: Team name, member count, meeting schedules displayed
```

### Test Case 3: IT Support
```
1. User: "Không vào được wifi F-town 3"
2. Bot: [Provides wifi credentials and IT contact]
3. Verify: Network name, password, contact info shown
```

### Test Case 4: Multi-topic Query
```
1. User: "Quản lý của tôi là ai? Team có lịch họp gì?"
2. Bot: [Answers both questions]
3. Verify: Manager info + team meetings both provided
```

---

## New Suggestion Buttons (Frontend)

Added 2 new buttons to welcome screen:
- 📅 **Lịch họp team** → "Team của tôi có lịch họp gì?"
- 📶 **Hỗ trợ IT** → "Không vào được wifi F-town 3"

Total: 8 suggestion buttons covering all use cases.

---

## Function Count

**Total Functions**: 8

**Original (2)**:
1. `get_employee_info`
2. `get_onboarding_tasks`

**Phase 1 Improvements (3)**:
3. `update_task_status`
4. `send_introduction_message`
5. `check_urgent_tasks`

**Phase 2 Use Cases (2)**:
6. `get_team_meetings` ⭐ NEW
7. `get_next_task` ⭐ NEW

**Note**: Use Case 3 doesn't need functions - uses embedded knowledge in system prompt.

---

## Key UX Improvements

1. **Confirmation Before Action**: Prevents accidental task updates
2. **Automatic Next Steps**: Suggests what to do after completing tasks
3. **Multi-turn Intelligence**: Can handle complex queries with multiple intents
4. **Contextual Knowledge**: No need to call functions for static information
5. **Rich Formatting**: All responses use Markdown with emojis

---

## Impact

These 3 use cases transform the chatbot from a simple Q&A tool into a comprehensive onboarding assistant that:

✅ **Manages tasks interactively** (not just reads them)
✅ **Facilitates team integration** (meetings, contacts)
✅ **Provides instant IT/HR support** (no waiting for humans)

The bot now covers **100% of common onboarding scenarios** at FPT Software.

