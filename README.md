<h1 align="center">🏙️ SafeCity Hub</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind">
</p>

<h3 align="center">A Multi-Stakeholder Crime Reporting, Monitoring & Real-Time Urban Safety Management Platform</h3>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h2 align="left">📖 Overview</h2>
<p align="left">
SafeCity Hub is a smart, integrated platform designed to improve urban safety by connecting citizens, police, and administrative authorities on a single digital system.<br>
It enables real-time crime reporting, incident monitoring, and data-driven decision-making to build safer, smarter cities.
</p>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h2 align="left">🚀 Key Features</h2>

### 🧑‍🤝‍🧑 Citizen Portal

- **Report Crimes**: Log safety concerns with exact locations and details.
- **Flexible Login**: Access accounts securely with either a User ID or Registered Email.
- **OTP Password Recovery**: Forgot your password? Instantly recover it via a secure 6-Digit Email OTP process with a glassmorphism UI.

### 👮 Police Dashboard

- **Live Monitoring**: Track incoming reported incidents in your specific jurisdiction in real-time.
- **Status Updates**: Automatically update and inform citizens regarding the resolution status of their complaints directly to their email.
- **Criminal Records**: Upload, manage, and attach images of known offenders securely.

### 🏛️ Admin Panel

- **Data Analytics**: Analyze crime data, visualize yearly trends on charts, and plan urban safety strategies.
- **Station Management**: Create regional police station sub-accounts dynamically.

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h2 align="left">🧩 System Architecture</h2>
<p align="left"><b>Primary Stakeholders:</b></p>
<ul>
    <li>Citizens</li>
    <li>Police / Law Enforcement</li>
    <li>Municipal & Administrative Authorities</li>
</ul>

<p align="left"><b>Workflow:</b></p>
<ol>
    <li>A citizen logs in/registers and reports an incident via the web portal.</li>
    <li>The system logs data securely to a cloud-ready PostreSQL database.</li>
    <li>Local police (matching the citizen's Area Code) receive real-time alerts and take action, emailing resolution statuses back to the citizen.</li>
    <li>Administrators access overarching analytics for macro policy planning.</li>
</ol>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">


<h2 align="left">⚙️ Installation & Setup</h2>

### 1. Requirements Checklist

- Python 3.10+
- PostgreSQL Server
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/vedangdhuri/SafeCity-Hub.git
cd SafeCity-Hub
```

### 3. Environment Variable Setup (.env)

Create a `.env` file at the root of your project directory to manage sensitive credentials:

```env
# Example .env configuration
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://YOUR_USERNAME:YOUR_PASSWORD@127.0.0.1:5432/crime_analysis

# Email Configurations for OTP
SET_EMAIL_HOST_USER=your_email@gmail.com
SET_EMAIL_HOST_PASSWORD=your_generated_app_password
SET_DEFAULT_FROM_EMAIL=your_email@gmail.com
```

_Note: Ensure your PostgreSQL has a database successfully created named `crime_analysis`._

### 4. Setup Python Environment

```bash
# Create the virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install all dependencies (django, psycopg2, django-dotenv, etc.)
pip install -r requirements.txt
```

### 5. Email OTP Setup

If using Gmail, go to `<a href="https://myaccount.google.com/apppasswords">App Passwords</a>` and generate a sequence. Add this generated 16-character password to `SET_EMAIL_HOST_PASSWORD` in your `.env` file along with your email address in `SET_EMAIL_HOST_USER` and `SET_DEFAULT_FROM_EMAIL`.

### 6. Migrate & Boot Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to explore the application!

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h2 align="left">❗ Note on Access Control</h2>
<p>
Role-Based Access Control (RBAC) securely limits data access. In the police portal, an officer from Station <code>001</code> can <b>only</b> view citizen complaints made within area code <code>001</code>.
</p>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h2>📜 License</h2>
<p>This project is licensed under the <a href="./LICENSE" target="_blank"><strong>MIT License</strong></a>.</p>
