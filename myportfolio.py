import streamlit as st
import requests

# Set the title and page configuration
st.set_page_config(page_title="Adarsh Koppa Manjunath - Python Developer | SDET", page_icon=":guardsman:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Skill Summary", "Work Experience", "Projects", "Education", "Contact"])

# Home Page
if page == "Home":
    st.title("Adarsh Koppa Manjunath")
    st.markdown("""
    **Python Developer | SDET | QA Automation**  
    [LinkedIn](https://www.linkedin.com/in/adarsh-koppa-m-740756326/) | [GitHub](https://github.com/adarshkoppamanjunath) | [HackerRank](https://www.hackerrank.com/profile/AdarshManjunath)  
    📧 [adarshakmkmanjunath@gmail.com](mailto:adarshakmkmanjunath@gmail.com) | 🌍 Edmonton, Canada
    """)
    st.subheader("Profile Summary")
    st.markdown("""
    • 6+ years of work experience as a test tool developer primarily using Python.  
    • Expertise in developing test/automation tools for API, CLI, UI, and DB interfaces using Python, PyTest, Requests, Selenium (POM), Postman, JMeter, and Robot Framework.  
    • Experience in designing and developing REST APIs using Flask and Django (MVC Framework).  
    • Experience with CI/CD setup using Docker, GitLab, Azure DevOps, and Kubernetes.  
    • Familiar with technologies like JIRA, VMs Docker, Azure DevOps, Jenkins, PostgreSQL, YAML, and OpenAPI.  
    • Completed certifications in JS, Python, Problem Solving, DevOps, Selenium, Robot Framework, and Docker.
    """)

    # GitHub URL to the raw resume file
    resume_url = "https://raw.githubusercontent.com/adarshkoppamanjunath/myportfolio/main/AdarshResume.pdf"  # Replace with actual URL

    # Add a download button for the resume
    st.markdown(f"[Download Resume]({resume_url})")
    
if page == "Skill Summary":
    st.title("🛠️ Skill Summary")
    st.markdown("### **Python Developer | SDET | QA Automation**")
    st.write("🚀 6+ years of experience in QA automation or test tool development")

    # Core Competencies
    with st.expander("🔹 **Core Competencies**", expanded=True):
        st.markdown("""
        - **Programming:** Python, JavaScript(basic)
        - **Automation Testing:** Pytest, Robot Framework, Selenium (POM), Requests, Postman, JMeter, Taurus
        - **REST API Development & Testing:** FAST API, Requests, Postman, JMeter
        - **CI/CD & DevOps:** Docker, Kubernetes, GitLab, Azure DevOps, Jenkins, GitHub Actions
        - **Performance & Load Testing:** JMeter, Taurus, AWS DLT
        - **Test Infrastructure & Tools:** VMs, Docker, Kubernetes, Azure DevOps, Jenkins
        - **Database & Backend Testing:** PostgreSQL, and MySQL
        - **Agile & SDLC:** Scrum, Sprint Planning, Retrospectives
        """)

    # Key Achievements
    with st.expander("🏆 **Key Achievements**", expanded=False):
        st.markdown("""
        - 🛠️ Developed a **custom automation framework using Robot Framework** for UI, API, SSH, and Kubernetes testing.
        - 🔥 Built a **Python-based REST API automation tool (PDS-CLIENT-SIM)** for train dispatch systems testing.
        - 🌐 Created internal **Flask-based APIs** for automation tools and test result storage.
        - 📊 Conducted **performance and load testing** using JMeter, Taurus, and AWS DLT.
        - 🎯 Led **QA automation for microservices**, designing test cases, executing tests, and reporting defects.
        """)

    # Certifications & Learning
    with st.expander("📜 **Certifications & Learning**", expanded=False):
        st.markdown("""
        - 🎖️ **Certified in Python (Advanced), REST API, and Problem Solving** - HackerRank
        - 🐳 **Docker Fundamentals Certification** - Kode Kloud
        - ☁️ **Microsoft Azure AI & DevOps Fundamentals** - AI-900, AZ-400
        - 📜 **JavaScript Algorithms & Data Structures Certification** - FCC
        - 🏆 **Python 3 Programming assessment (95%)** - IKM
        """)

    # Footer
    st.markdown("---")
    st.markdown("🚀 **Let's connect and collaborate!** [LinkedIn](https://www.linkedin.com/in/adarsh-koppa-m-740756326/) | [GitHub](https://github.com/adarshkoppamanjunath) | 📧 [Email](mailto:adarshakmkmanjunath@gmail.com)")

# Work Experience Page
if page == "Work Experience":
    st.title("💼 Work Experience")
    
    # Willowglen Systems
    with st.expander("**Software Developer in Test | Willowglen Systems (Aug 2023 - Present)**"):
        st.markdown("""
        - Working on the SentientQ project, introducing microservices into a legacy monolithic product (SCADACOM).  
        - Developed an automation framework from scratch using Robot Framework and CI/CD with GitLab, Docker, and shell scripts.  
        - Responsible for test case development, execution, and collaboration in an agile environment.  
        - Worked in reverse engineering to gather requirements, prepare test cases, and execute them.  
        - Developed automation collections using Postman and JavaScript for API test cases and ran them using Postman container.  
        - Involved in QA ownership for certain services, creating and executing test scenarios and discussing results with the team.
        """)

    # Trustwave
    with st.expander("**Software Developer in Test | Trustwave (Apr 2022 - Jul 2023)**"):
        st.markdown("""
        - Developed internal test tools for SIEM components and created REST API endpoints using Flask.  
        - Automated tests for API, UI, DB, and CLI using Python, Robot, and Selenium.  
        - Load testing for MISP APIs with JMeter, Taurus, and AWS DLT.  
        - Developed tools for storing test results and updating Confluence, JIRA, etc., using APIs and shell scripts.  
        - Involved in Infra setup, troubleshooting, and debugging in VM and AWS environments.
        """)

    # CNR
    with st.expander("**Software Developer 2 | CNR (Jan 2021 - Jan 2022)**"):
        st.markdown("""
        - Developed a Python-based tool, PDS-CLIENT-SIM, for REST and WebSocket automation.  
        - Built stress and load testing tools and integrated pipelines using Docker and Azure DevOps.  
        - Contributed to API review meetings from an automation perspective and helped team members with debugging and understanding new requirements.  
        - Involved in the creation of internal APIs using Flask.
        """)

    # Dell EMC
    with st.expander("**Software Engineer 2 | Dell EMC (Feb 2016 – Dec 2018)**"):
        st.markdown("""
        - Developed and maintained the NGM framework for REST API testing.  
        - Contributed to network, device, and power feature testing for Dell PowerEdge MX servers.  
        - Automated UI tests using Selenium and Java.  
        - Developed tools for Stress and Load testing using Python.  
        - Prepared and executed automation test suites using Jenkins for Build Verification and Regression Testing.  
        - Involved in test environment setup and debugging servers with the required configurations.
        """)

# Projects Page
if page == "Projects":
    st.title("🛠️ Projects")
    st.markdown("### GitHub Repositories")
    st.markdown("""
    Here are some of the projects I’ve worked on. Click on the links to explore the repositories.
    """)

    # Fetch the project list from GitHub
    repo_url = "https://api.github.com/users/adarshkoppamanjunath/repos"
    repos = requests.get(repo_url).json()

    # List all projects (excluding data compression)
    exclude_repos = ['data_compression','myportfolio']  # List repos to exclude
    for repo in repos:
        if repo['name'].lower() not in exclude_repos:
            with st.expander(f"#### [{repo['name']}]({repo['html_url']})"):
                # Summarize the description based on the repo name keywords
                repo_name = repo['name'].lower()
                if 'k8-ms' in repo_name:
                    st.markdown("🚀 **Kubernetes Microservices**<br>"
                                "🛠️ This repo consists of **Kubernetes deployment files** for microservices, including:<br>"
                                "🔹 **FastAPI** (⚡) with SQLite backend for inventory CRUD APIs<br>"
                                "🔹 **Streamlit** (📊) as the front end<br>"
                                "🔹 **Robot Framework** (🤖) for automation tests",
                                unsafe_allow_html=True)

                elif 'python-fast-apis' in repo_name:
                    st.markdown("⚡ **FastAPI with SQLite Deployment on Render**<br>"
                                "🔐 Includes **JWT authentication** and **authorization**<br>"
                                "📊 Provides **CRUD endpoints** with **rate limiting**<br>"
                                "🔗 [Access FastAPI Docs](https://python-flask-apis.onrender.com/docs)",
                                unsafe_allow_html=True)

                elif 'postman-rest-api-tests' in repo_name:
                    st.markdown("📮 **Postman API Testing Collection**<br>"
                                "🛠️ Helps in testing **REST API endpoints** using Postman<br>"
                                "🔹 How to set variables<br>"
                                "🔹 How to validate API responses (status codes, data, etc.)<br>"
                                "🔹 Example of chaining API calls (e.g., DELETE → GET verification)",
                                unsafe_allow_html=True)

                elif 'robot' in repo_name:
                    st.markdown("🤖 **Robot Framework Automation**"
                                "🛠️ Includes **Selenium** (🌐) and **Requests Library** for UI & API automation")

                elif 'pytest-selenium-request' in repo_name:
                    st.markdown("🧪 **Pytest Automation Framework**<br>"
                                "🛠️ Helps in setting up **UI & API testing** using **Pytest** (🐍), **Selenium** (🌐), and **Requests",
                                unsafe_allow_html=True)

                elif 'python-streamlit' in repo_name:
                    st.markdown("📊 **Streamlit Web App Example**<br>"
                                "🔐 Includes **JWT-based authentication** and **CRUD operations**<br>"
                                "⚡ Backend powered by **FastAPI**<br>"
                                "🔗 [FastAPI Repo](https://github.com/adarshkoppamanjunath/Python-Fast-APIs)",
                                unsafe_allow_html=True)


# Education Page
if page == "Education":
    st.title("🎓 Education")

    # Master's Degree
    with st.expander("🎓 **Master’s Degree in Computer Science**"):
        st.markdown("""
        University of Regina | **83.3%**  
        Courses: Software Development, Data Science, Image Processing, and Computer Networking related fields.
        """)

    # Bachelor's Degree
    with st.expander("🎓 **Bachelor’s Degree in Information Technology**"):
        st.markdown("""
        UVCE | **72.65%**  
        Courses: Programming Languages (C, C++, Java, PHP, C#), Data Structures, Algorithms, OOPs, Database Systems, and Web Development.
        """)

if page == "Contact":
    st.title("📬 Contact Me")

    st.markdown("""
    If you would like to get in touch, feel free to use the form below to send me a message!
    """)

    # Create a form
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        # Submit button
        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name and email and message:
                # Set up the EmailJS API
                emailjs_url = "https://api.emailjs.com/api/v1.0/email/send"
                payload = {
                    "service_id": st.secrets["service_id"],   # Replace with your EmailJS Service ID
                    "template_id":  st.secrets["template_id"],  # Replace with your EmailJS Template ID
                    "user_id":st.secrets["user_id"] ,          # Replace with your EmailJS User ID
                    "template_params": {
                        "user_name": name,
                        "user_email": email,
                        "message": message
                    }
                }

                # Send the email
                response = requests.post(emailjs_url, json=payload)

                if response.status_code == 200:
                    st.success("Your message has been sent successfully!")
                else:
                    st.error("Oops! Something went wrong. Please try again later.")
            else:
                st.error("Please fill in all fields.")

# Footer Section (for all pages)
st.markdown("""
Thanks for visiting my portfolio! Feel free to reach out via email or GitHub for collaborations, opportunities, or further discussions.
""")