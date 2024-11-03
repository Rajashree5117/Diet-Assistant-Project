# Diet Assistant Project
The **Diet Assistant App** is a Django-based web application that allows users to connect with dieticians for personalized diet plans based on their **age** and **BMI**.

## Key Features:
  **User Registration and Role Assignment**
  • Users can register, and after registration, they are initially assigned the role of a "Guest."
  • Users can request an upgrade in role (either "User" or "Dietician") by sending a message to the superuser, who manually updates roles accordingly.

  **Personalized Diet Plan Requests**
  • Users can view available dieticians who provide diet suggestions based on age and BMI.
  • Users can send a personalized request to a dietician, specifying details like health issues, age, and BMI.
  • Dieticians receive this request in the form of an email notification, containing all the necessary user information for reference.
  
  **Email-Based Communication for Diet Plans**
  • Instead of in-app notifications, the dietician sends the tailored diet plan directly to the user’s email.
  • This email includes customized diet recommendations based on the user’s health details, ensuring privacy and direct delivery.
  
  **Diet Management for Dieticians**
  • Dieticians can manage their diet plans within the app, with options to add, edit, or delete diets.
  • Each diet plan includes fields for age range, BMI range, health issue focus, and a detailed description of the plan.
  
  **Profile Management**
  • Both users and dieticians can update their profiles to reflect changes in personal information or health status.
  • New profile data, such as BMI or health issue updates, can influence the diet recommendations they receive.
  
  **Messaging Mechanism with Superuser and Dieticians**
  • Users can communicate with the superuser through the messaging system to request role changes.
  • The app’s messaging feature ensures that all relevant details (like age, BMI, and health issues) are captured in the user’s messages.
  
  **User-Friendly Navigation**
  • The app features an intuitive navbar with easy access to Home, About, Contact, Register, and BMI Calculator pages.
  • Once registered, users can access additional options, like viewing diet suggestions and managing profiles.

## Technologies Used:
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (development)
- **Messaging System:** Django Models
**https://docs.google.com/presentation/d/1UwCturmkRN-B47CMkl3JVoMDj-VgDhtW/edit?usp=drive_link&ouid=100018126142864796718&rtpof=true&sd=true**
