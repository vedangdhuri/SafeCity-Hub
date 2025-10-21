<h1 align="left">🏙️ SafeCity Hub</h1>
<h3 align="left">A Multi-Stakeholder Crime Reporting, Monitoring & Real-Time Urban Safety Management Platform</h3>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">📖 Overview</h1>
<h3 align="left">SafeCity Hub is a smart, integrated platform designed to improve urban safety by connecting citizens, police, and administrative authorities on a single digital system.
It enables real-time crime reporting, incident monitoring, and data-driven decision-making to build safer, smarter cities.</h3>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">🚀 Key Features</h1>
<ul>
    <li>🧑‍🤝‍🧑 Citizen Portal: Report crimes or safety concerns with location, images, or videos (anonymously or identified).</li>
    <li>👮 Police Dashboard: Live monitoring of reported incidents, response assignment, and communication tools.</li>
    <li>🏛️ Admin Panel: Analyze crime data, visualize heatmaps, and plan urban safety strategies.</li>
</ul>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">🧩 System Architecture</h1>
<h3 align="left">Stakeholders:</h3>
<ul>
    <li>Citizens</li>
    <li>Police / Law Enforcement</li>
    <li>Municipal & Administrative Authorities</li>
</ul>

<h3 align="left">Stakeholders:</h3>
<ol>
    <li>A citizen reports an incident via web/app.</li>
    <li>The system logs data in the central database.</li>
    <li>Police receive real-time alerts and take action.</li>
    <li>Administrators access analytics for policy planning.</li>
</ol>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1>🛠️ Tech Stack</h1>
<table>
    <tr>
        <td><b>Frontend</b></td>
        <td>
            <img src="https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white" alt="HTML">
            <img src="https://img.shields.io/badge/CSS-639?logo=css&logoColor=fff" alt="CSS">
            <img src="https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff" alt="Bootstrap">
        </td>
    </tr>
    <tr>
        <td><b>Backend</b></td>
        <td>
            <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python">
            <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000" alt="JavaScript">
            <img src="https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white" alt="Django">
        </td>
    </tr>
    <tr>
        <td><b>Database</b></td>
        <td>
            <img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff" alt="MySQL">
        </td>
    </tr>
    <tr>
        <td><b>Code Editor</b></td>
        <td>
            <img src="https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white" alt="VS Code">
            <img src="https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff" alt="PyCharm">
        </td>
    </tr>
</table>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">⚙️ Installation & Setup</h1>

1. Clone the repository:
    ```bash
    git clone https://github.com/vedangdhuri/SafeCity-Hub.git
    cd SafeCity-Hub
    ```

2. Software Installation
    ```bash
    start /wait python-3.6.2-amd64.exe
    ```
    ```bash
    start /wait Wampserver2.4-x64.exe
    ```

3. WampServer setup
    - Open WampServer
    - To access : Go to localhost/phpmyadmin in your browser
    - Username : root
    - Password : Leave the field completely empty
    - Create a database named "crime_analysis"
    - **❗ IMPORTANT Note** : To ensure your project runs smoothly, be sure to launch the WampServer software at the start. 

4. Email Sending setup
    - Open crime_analysis folder
    - Open emailsetting.py
    - Enter your email here [ SET_EMAIL_HOST_USER = 'youremail@gmail.com' ]
    - Enter your app password here [ SET_EMAIL_HOST_PASSWORD = 'your app pass word' ]
    - If you're unsure how to create an app password, please watch this video for guidance <a href="https://youtu.be/MkLX85XU5rU?si=VH0IeGVYaUHZkIDk">Link</a>

5. Start the project
    <h4>❗ IMPORTANT Note : If you're creating a virtual environment in VS Code, choose Python version 3.6.2.</h4>
    
    ```bash
    python -m venv venv
    ```
    ```bash
    venv/Scripts/activate
    ```
    ```bash
    py manage.py makemigrations
    ```
    ```bash
    py manage.py migrate
    ```
    ```bash
    py manage.py runserver
    ```

6. Open your browser and navigate to:
    ```bash
    http://127.0.0.1:8000/
    ```
<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">❗ Additional Note</h1>

<p>In the area police station, only the police of area code 001 can view the complaints. Police from other areas (002 or 003) cannot access these complaints.</p>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">🔐 Security & Privacy</h1>
<ul>
    <li>End-to-end encrypted communication</li>
    <li>Role-based access control (Citizen, Police, Admin)</li>
    <li>Option for anonymous reporting</li>
    <li>Data protection compliant with standard security guidelines</li>
</ul>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">💡 Future Enhancements</h1>
<ul>
    <li>AI-based crime prediction and pattern recognition</li>
    <li>IoT integration (smart CCTV, panic buttons)</li>
    <li>Chatbot for emergency help</li>
    <li>Integration with government databases for automated response</li>
</ul>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">🏆 Impact</h1>
<ul>
    <li>Faster law enforcement response</li>
    <li>Improved citizen safety engagement</li>
    <li>Data-driven urban policy planning</li>
    <li>Transparent communication between authorities and citizens</li>
</ul>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">🏁 OUTPUT</h1>
<img src="https://github.com/vedangdhuri/images/blob/main/safecityhub-op-git.gif?raw=true" alt="Header" width="1011" height="auto">


<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1 align="left">👨‍💻 Contributors</h1>

<ul>
  <li><strong>Project Title:</strong> SafeCity Hub – A Multi-Stakeholder Crime Reporting and Urban Safety Platform</li>

  <li><strong>Project Team Members:</strong></li>
  <ul>
    <li>
      <a href="https://github.com/vedangdhuri" target="_blank">
        <strong>Vedang Dhuri</strong>
      </a> – <em>Team Leader & Technical Head</em><br>
      Responsible for overall project architecture, backend development, database design, and integration of all technical modules.
    </li>
    <li>
        <a href="https://github.com/urvee1306" target="_black">
        <strong>Urvee Andurlekar</strong>
        </a> - <em>UI/UX Designer and Frontend Developer</em>
    </li>
    <li>
        <a href="https://github.com/YashBhurke" target="_blank">
            <strong>Yash Bhurke</strong> 
        </a> - Admin Dashboard & Data Analytics Module
    </li>
    <li><strong>Saish Desai</strong> – Database Management & Testing</li>
    <li><strong>Santoshi Haldankar</strong> – Quality Assurance, Documentation & Deployment</li>
  </ul>
</ul>

<hr style="height:2px;border-width:0;color:gray;background-color:gray;margin-top:20px;margin-bottom:20px">

<h1>📜 License</h1>
<p>This project is licensed under the <a href="./LICENSE" target="_blank"><strong>MIT License</strong></a>.</p>
