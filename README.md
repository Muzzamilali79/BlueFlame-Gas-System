# BlueFlame Gas - Gas Supply Management System 🔥

## 📋 Project Description
BlueFlame Gas is a web-based Gas Supply Management System designed to streamline the process of booking and delivering gas cylinders. It provides a user-friendly interface for customers to place orders and track their status, while offering a comprehensive dashboard for administrators to manage stock, orders, and customer queries efficiently.

## 🚀 Features

### 👤 User Panel (Customer)
* **Secure Authentication:** User Registration and Login.
* **Book Cylinder:** Easy booking interface with auto-bill calculation.
* **Order History:** View past orders.
* **Track Status:** Real-time status updates (Pending -> Approved -> Delivered).
* **Contact Support:** Direct messaging system for complaints.

### 🛠 Admin Panel
* **Dashboard:** Overview of total orders and pending requests.
* **Order Management:** Approve or Update order status with one click.
* **User Management:** View registered customers.
* **Feedback System:** View and reply to customer messages.

## 💻 Technologies Used
* **Backend:** Python (Django Framework)
* **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
* **Database:** SQLite (Default)
* **Version Control:** Git & GitHub

## ⚙️ How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/BlueFlame-Gas-System.git](https://github.com/YOUR_USERNAME/BlueFlame-Gas-System.git)
    cd BlueFlame-Gas-System
    ```

2.  **Create Virtual Environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    # source venv/bin/activate  # For Mac/Linux
    ```

3.  **Install Requirements:**
    ```bash
    pip install django
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create Superuser (Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run Server:**
    ```bash
    python manage.py runserver
    ```

## 👨‍💻 Developed By
**Muzzamil Ali** 
BS Computer Science
FUUAST Islamabad
