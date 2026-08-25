# Support Ticket Hub - Visual Guide & How It Works

## 🎯 Application Flow

```
User visits http://localhost:3000
         ↓
    [Not logged in?]
         ↓
    Login/Register Page
         ↓
    [Enter credentials]
         ↓
    Backend validates (Flask API)
         ↓
    JWT token returned
         ↓
    [Token saved to localStorage]
         ↓
    Dashboard Page
         ↓
    [User can navigate to Tickets or Create Ticket]
```

---

## 📱 Page Breakdown

### 1️⃣ LOGIN / REGISTER PAGE

**URL:** `http://localhost:3000/login`

**What you see:**
```
┌─────────────────────────────────────────────┐
│                                             │
│         🎫 Support Ticket Hub              │
│    IT Support Management System            │
│                                             │
│  ┌─────────────────────────────────────┐  │
│  │  [LOGIN]  [REGISTER]                │  │
│  ├─────────────────────────────────────┤  │
│  │                                     │  │
│  │  Username: [________________]       │  │
│  │  Password: [________________]       │  │
│  │                                     │  │
│  │  ┌──────────────────────────────┐  │  │
│  │  │      LOGIN BUTTON            │  │  │
│  │  └──────────────────────────────┘  │  │
│  │                                     │  │
│  │  Demo Credentials:                  │  │
│  │  Username: demo                     │  │
│  │  Password: demo123                  │  │
│  │                                     │  │
│  └─────────────────────────────────────┘  │
│                                             │
│  Built with ❤️ for IT Support Teams       │
│                                             │
└─────────────────────────────────────────────┘
```

**Features:**
- Tab to switch between Login & Register
- Real-time form validation
- Password strength indicators
- Error/Success messages
- Auto-redirect after login

**Register Tab Adds:**
- Email field
- Full Name field
- Confirm Password field
- Password validation (min 6 chars)

---

### 2️⃣ DASHBOARD PAGE

**URL:** `http://localhost:3000/dashboard` (Auto-redirect after login)

**What you see:**

```
┌────────────────────────────────────────────────────────────────┐
│ 🎫 Support Ticket Hub              [User: demo] [Logout Button]│
│ Dashboard                                                       │
└────────────────────────────────────────────────────────────────┘

Welcome back, Demo Admin! 👋
Here's an overview of your support tickets

┌──────────────┬──────────────┬──────────────┬──────────────┐
│   📋         │   🔴         │   ⏳         │   ✅         │
│ TOTAL        │ OPEN         │ IN PROGRESS  │ CLOSED       │
│ TICKETS      │ TICKETS      │ TICKETS      │ TICKETS      │
│              │              │              │              │
│     15       │      3       │      2       │     10       │
└──────────────┴──────────────┴──────────────┴──────────────┘

┌──────────────────────────────────────────────────────────────┐
│ [+ Create New Ticket]  [📋 View All Tickets]                │
└──────────────────────────────────────────────────────────────┘

Recent Tickets
┌─────────────────────────────────────────────────────────────┐
│ ID │ Title                          │ Status │ Priority      │
├────┼────────────────────────────────┼────────┼───────────────┤
│ #1 │ Cannot login to system         │ OPEN   │ 🟠 HIGH      │
│    │ Getting error: Invalid cred... │        │               │
├────┼────────────────────────────────┼────────┼───────────────┤
│ #2 │ Database connection error      │ IN PRO │ 🔴 CRITICAL  │
│    │ Timeout on dashboard page...   │        │               │
├────┼────────────────────────────────┼────────┼───────────────┤
│ #3 │ Feature request: Dark mode     │ OPEN   │ 🟢 LOW       │
│    │ Many users have requested...   │        │               │
└─────────────────────────────────────────────────────────────┘
```

**Stats Shown:**
- Total Tickets Count
- Open Tickets (Red icon)
- In Progress Count (Yellow icon)
- Closed/Resolved Count (Green icon)

**Quick Actions:**
- "Create New Ticket" button
- "View All Tickets" button

**Recent Tickets Table:**
- Shows last 5 tickets
- Color-coded status badges
- Color-coded priority badges
- Click row to view details (future feature)

---

### 3️⃣ TICKETS PAGE

**URL:** `http://localhost:3000/tickets`

**What you see:**

```
┌────────────────────────────────────────────────────────────────┐
│ ← All Tickets                              [User: demo] [Logout]│
│    15 tickets                                                   │
└────────────────────────────────────────────────────────────────┘

[+ Create New Ticket]

FILTERS & SEARCH
┌──────────────┬──────────────┬──────────────┬──────────────┬────┐
│ Search       │ Status       │ Priority     │ Sort By      │Ord │
│ [________]   │ [All]      ▼ │ [All]      ▼ │ Date       ▼ │Desc│
│              │              │              │              │    │
│ Title or     │ • Open       │ • Critical   │ • Created    │• N │
│ description  │ • In Prog    │ • High       │ • Title      │ewes│
│              │ • Resolved   │ • Medium     │ • Priority   │t F │
│              │              │ • Low        │ • Status     │irs │
└──────────────┴──────────────┴──────────────┴──────────────┴────┘

[Clear all filters]

ALL TICKETS
┌──────┬─────────────────────────┬──────────┬──────────┬──────────┐
│ ID   │ Title                   │ Status   │Priority  │ Assigned │
├──────┼─────────────────────────┼──────────┼──────────┼──────────┤
│ #15  │ Email sync issues       │ ON HOLD  │ MEDIUM   │ agent1   │
│ #14  │ Cannot login            │ OPEN     │ HIGH     │ Unassign │
│ #13  │ Feature: Dark mode      │ OPEN     │ LOW      │ Unassign │
│ #12  │ Printer not working     │ RESOLVED │ MEDIUM   │ agent1   │
│ #11  │ Database error          │ IN PRO   │ CRITICAL │ agent1   │
│  ... │ ... more tickets ...    │ ...      │ ...      │ ...      │
└──────┴─────────────────────────┴──────────┴──────────┴──────────┘

Showing 15 of 15 ticket(s)
```

**Search & Filter Features:**
- Real-time search by title/description
- Filter by Status (Open, In Progress, On Hold, Closed, Resolved)
- Filter by Priority (Critical, High, Medium, Low)
- Sort options (Date, Title, Priority, Status)
- Sort order (Newest/Oldest first)
- "Clear all filters" button
- Shows result count

**Color Coding:**
- Status badges: Red (Open), Yellow (In Progress), Green (Resolved)
- Priority badges: Red (Critical), Orange (High), Yellow (Medium), Green (Low)

**Table Columns:**
- ID (Ticket number)
- Title (Truncated with description snippet)
- Status (Color-coded)
- Priority (Color-coded)
- Created By
- Assigned To
- Created Date

---

### 4️⃣ CREATE TICKET PAGE

**URL:** `http://localhost:3000/tickets/new`

**What you see:**

```
┌────────────────────────────────────────────────────────────────┐
│ ← Create New Ticket                        [User: demo] [Logout]│
│    Submit a support request                                    │
└────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                                                              │
│ Ticket Title *                                               │
│ ┌────────────────────────────────────────────────────────┐  │
│ │ Brief summary of your issue                            │  │
│ │                                              0/200 chars│  │
│ │ Minimum 5 characters. Be specific and descriptive.    │  │
│ └────────────────────────────────────────────────────────┘  │
│                                                              │
│ Description *                                                │
│ ┌────────────────────────────────────────────────────────┐  │
│ │ Provide detailed information:                          │  │
│ │ - What is the problem?                                 │  │
│ │ - When did it occur?                                   │  │
│ │ - What have you tried?                                 │  │
│ │ - Any error messages?                                  │  │
│ │                                                        │  │
│ │                                                        │  │
│ │                                        0/2000 chars    │  │
│ │ Minimum 10 characters. More details = better help.   │  │
│ └────────────────────────────────────────────────────────┘  │
│                                                              │
│ Priority Level                                               │
│ ┌────────────────────────────────────────────────────────┐  │
│ │ 🟢 Low - General inquiry, no urgency            ▼     │  │
│ │                                                        │  │
│ │ Other options:                                         │  │
│ │ 🟡 Medium - Important but not critical                │  │
│ │ 🟠 High - Significant impact on work                  │  │
│ │ 🔴 Critical - System down, blocking work              │  │
│ └────────────────────────────────────────────────────────┘  │
│                                                              │
│ ┌──────────────────────────────────────────────────────┐   │
│ │ 💡 Tip: Provide as much info as possible for faster  │   │
│ │        resolution by our support team.               │   │
│ └──────────────────────────────────────────────────────┘   │
│                                                              │
│ ┌────────────────────────────┬──────────────────────────┐   │
│ │  [Create Ticket]           │     [Cancel]             │   │
│ └────────────────────────────┴──────────────────────────┘   │
│                                                              │
└──────────────────────────────────────────────────────────────┘

TIPS FOR CREATING EFFECTIVE TICKETS
1. Be specific - Avoid vague descriptions
2. Include steps to reproduce - List exact steps
3. Provide error messages - Copy and paste them
4. Mention your environment - Browser, OS, software version
5. Set realistic priority - Be honest about urgency
```

**Form Features:**
- Title field (200 char limit with counter)
- Description field (2000 char limit with counter)
- Priority dropdown with descriptions and emojis
- Real-time validation
- Character count display
- Submit/Cancel buttons
- Loading spinner when submitting
- Helpful tips section
- Auto-redirect after successful submission

---

## 🔄 User Journey Example

### Scenario: User Reports a Bug

1. **User logs in:**
   - Goes to http://localhost:3000/login
   - Enters: `user1` / `user123`
   - ✅ Redirected to Dashboard

2. **User views Dashboard:**
   - Sees ticket statistics
   - Sees recent tickets
   - Decides to create a new ticket

3. **User creates a ticket:**
   - Clicks "Create New Ticket"
   - Goes to http://localhost:3000/tickets/new
   - Fills in form:
     - Title: "Cannot export reports to PDF"
     - Description: "When I try to export a report to PDF format, the system crashes. Happens every time. Error: OutOfMemory exception."
     - Priority: High
   - Submits form
   - ✅ Ticket created successfully (#16)
   - Auto-redirected to Tickets page

4. **Support agent views ticket:**
   - Agent logs in with `agent1` / `agent123`
   - Goes to Tickets page
   - Searches for "export"
   - Finds ticket #16
   - Clicks to view details (future feature)
   - Assigns to self
   - Starts working on it

---

## 🎨 Visual Theme

### Colors Used:
- **Primary Blue:** `#2563eb` - Buttons, headers, highlights
- **Red:** Error messages, critical priority, open tickets
- **Yellow:** In Progress status, medium priority
- **Green:** Success messages, resolved status, low priority
- **Orange:** High priority
- **Gray:** Neutral elements, secondary text

### Typography:
- Headers: Bold, larger sizes
- Body text: Regular weight
- Labels: Medium weight, smaller
- Error/Success text: Color-coded

### Spacing:
- Clean whitespace
- 6px, 12px, 16px, 24px grid
- Padding inside cards
- Gaps between elements

---

## 📊 Data Flow

```
FRONTEND                          BACKEND                      DATABASE
                                
Login Page ──────────────┐
                         │ POST /api/auth/login
                         ├──────────────────→ Flask Server ──→ PostgreSQL
                         │                    (Validate creds) │ Check users table
                         │                    │                │
                         │← JWT Token ←───────┴────────────────┘
                         │
              Store in localStorage
                         │
Dashboard ◄──────────────┘
                         │
                         │ GET /api/tickets
List Page ────────────────├──────────────────→ Flask Server ──→ PostgreSQL
                         │                    (With JWT) │ Query tickets
                         │                    │                │
                         │← Tickets JSON ◄────┴────────────────┘
                         │
Create Form ──────────────┤
                         │ POST /api/tickets
                         ├──────────────────→ Flask Server ──→ PostgreSQL
                         │                    (Create new) │ Insert row
                         │                    │                │
                         │← Success Message ◄─┴────────────────┘
                         │
              Redirect to Tickets Page
                         │
Dashboard ◄──────────────┘
```

---

## 🌐 How Backend & Frontend Communicate

### Example: Creating a Ticket

**Frontend (React):**
```javascript
// User clicks "Create Ticket"
// Form data:
const formData = {
  title: "Cannot export reports to PDF",
  description: "System crashes when exporting...",
  priority: "high"
}

// API call with JWT token
axios.post('/api/tickets', formData, {
  headers: { Authorization: `Bearer ${token}` }
})
```

**Backend (Flask):**
```python
# Receives request at POST /api/tickets
@tickets_bp.route('', methods=['POST'])
@jwt_required()  # Validates JWT token
def create_ticket():
    data = request.get_json()
    # Validate data
    # Create Ticket object
    # Save to PostgreSQL
    # Return response with ticket ID
```

**Response sent back to Frontend:**
```json
{
  "message": "Ticket created successfully",
  "ticket": {
    "id": 16,
    "title": "Cannot export reports to PDF",
    "status": "open",
    "priority": "high",
    "created_at": "2026-08-25T06:45:00Z"
  }
}
```

---

## 💾 Database Schema

```
USERS TABLE
┌──────────┬──────────────┬─────────────┬──────────┐
│ id (PK)  │ username     │ email       │ role     │
├──────────┼──────────────┼─────────────┼──────────┤
│ 1        │ demo         │ demo@ex.com │ admin    │
│ 2        │ agent1       │ agent@ex.cm │ agent    │
│ 3        │ user1        │ user@ex.com │ user     │
└──────────┴──────────────┴─────────────┴──────────┘

TICKETS TABLE
┌──────────┬──────────────┬──────────┬──────────┬──────────────┐
│ id (PK)  │ title        │ status   │ priority │ created_by   │
├──────────┼──────────────┼──────────┼──────────┼──────────────┤
│ 1        │ Cannot login │ open     │ high     │ 3 (user1)    │
│ 2        │ DB error     │ in_prog  │ critical │ 3 (user1)    │
│ 3        │ Dark mode    │ open     │ low      │ 3 (user1)    │
└──────────┴──────────────┴──────────┴──────────┴──────────────┘

COMMENTS TABLE
┌──────────┬──────────┬──────────┬──────────────┐
│ id (PK)  │ content  │ ticket_id│ author_id    │
├──────────┼──────────┼──────────┼──────────────┤
│ 1        │ "Can..." │ 1        │ 2 (agent1)   │
└──────────┴──────────┴──────────┴──────────────┘
```

---

## 🚀 What Happens When You Run It

### Terminal 1 (Backend):
```
$ python run.py
 * Running on http://0.0.0.0:5000
 * Debug mode: on
 * In-memory SQLite unless PostgreSQL configured
```

### Terminal 2 (Frontend):
```
$ npm start
Compiled successfully!

Local: http://localhost:3000
```

### Browser (http://localhost:3000):
1. Page loads
2. Checks localStorage for JWT token
3. If no token → Shows Login page
4. If token exists → Fetches dashboard data from backend
5. Shows Dashboard with stats & recent tickets
6. You can:
   - Create new ticket
   - View all tickets with filters
   - Search & sort
   - Logout (clears token)

---

## ✨ Key Interactions

| Action | Page | What Happens |
|--------|------|--------------|
| Click Logo | Any | Go to Dashboard |
| Click "Create New Ticket" | Dashboard/Tickets | Go to Create form |
| Fill & submit form | Create Page | API call → Ticket saved → Redirect |
| Type in search | Tickets Page | Real-time filter results |
| Select filter | Tickets Page | Filter updates instantly |
| Click row | Tickets Page | (Future) Open ticket details |
| Click Logout | Any | Clear token → Redirect to Login |

---

This is your complete full-stack application! 🎉
