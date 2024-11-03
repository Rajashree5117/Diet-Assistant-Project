# Diet Assistant Project
The **Diet Assistant App** is a Django-based web application that allows users to connect with dieticians for personalized diet plans based on their **age** and **BMI**.

## Key Features:
  **User Registration and Role Assignment**
  • Users can register, and after registration, they are initially assigned the role of a "Guest."
  • Superuser, who manually updates roles to either "User" or "Dietician" accordingly.

  **Personalized Diet Plan Requests**
  • Users can view available dieticians who provide diet suggestions based on age and BMI.
  • Users can send a personalized request to a dietician, specifying details like health issues, age, and BMI.
  • Dieticians receive this request containing all the necessary user information for reference.
  
  **Diet Management for Dieticians**
  • Dieticians can manage their diet plans within the app, with options to add, edit, or delete diets.
  • Each diet plan includes fields for age range, BMI range, health issue focus, and a detailed description of the plan.
  
  **Profile Management**
  • Both users and dieticians can update their profiles to reflect changes in personal information or health status.
  • New profile data, such as BMI or health issue updates, can influence the diet recommendations they receive.
  
  **User-Friendly Navigation**
  • The app features an intuitive navbar with easy access to Home, About, Contact, Register, and BMI Calculator pages.
  • Once registered, users can access additional options, like viewing diet suggestions and managing profiles.

## Technologies Used:
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (development)

**https://docs.google.com/document/d/1i24awsGNSoZSS7r8_siTvypnOXcbXfFFVp9mynPke_4/edit?usp=drive_link**
