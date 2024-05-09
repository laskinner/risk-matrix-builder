# Causa -- A Risk Management Tool

Causa is a Django-based web application focused on identifying, cataloging, and mitigating various hazards and their associated outcomes. Designed for risk management professionals operating in high-stakes enivornemnts, such as human space flight, Causa offers a platform to catalog and discuss potential risks in various outcomes. The best way to use Causa is to delpoy the repo, deploy, and begin adding hazards and outcomes on the appropriate subject matter. Admins can contribute by adding hazards, detailing their probability and severity, and suggesting potential outcomes. The community aspect of Causa allows for a collaborative approach, where users can comment on and discuss each hazard, providing insights and solutions. This interactive environment makes Causa not just a risk assessment tool, but also a hub for learning and sharing knowledge about risk management in a dynamic, user-friendly interface.


![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/05dc9ac1-257b-4dfb-a6b1-15c7ccff6c34)

[Link to Live Site]([url](https://risk-matrix-builder-e54f9998e9bb.herokuapp.com/))


# Causa Project Readme

## Features

### Existing Features

#### Navigation Bar
- Featured across all pages for easy and consistent navigation.
- Enhances user experience by allowing seamless access to various sections of the site.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/c82b816f-3b0f-48b0-96ba-0fa23d151eca)


#### Hazard and Outcome Lists
- Displays user-contributed hazards and outcomes in an organized manner.
- Aids users in quickly identifying and accessing specific risks and their details.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/f7953510-512b-4a96-8ff8-327626523476)

Both the Hazard and Outcome List views are based upon the following mock-up:
![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/b8a808b6-a776-45ed-a03c-8e766dad1870)


#### Hazard and Outcome Detail Pages
- Provides comprehensive information about each hazard and outcome.
- Includes user comments and discussions, fostering a community-focused environment.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/ca9cd8b7-6d87-40a9-bad6-0b6e43a5b6d9)

Both and Hazard and Outcome Detail pages are bosed upon the following mock-up:
![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/f5bb5d2c-06f9-494e-b55f-b0c251f9d370)



#### Comment System
- Engages users by allowing them to share insights and experiences related to various hazards and outcomes.
- Strengthens the community aspect of the platform.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/afb2bd76-6186-4d9d-9172-f33276127399)


#### User Authentication
- Ensures a secure and personalized user experience.
- Allows users to contribute and interact with content based on their interests and expertise.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/0b3aa621-9720-43bc-99fb-2ba433e7e47c)

#### Document Management
- Allows admins to upload supporting documents, such as scientific papers or research, to specific hazards and outcomes.
- Allows users to download supporting documents through the UI.

#### Description
- Allows admins to create valuable descriptions for hazards and outcomes.
- Allows users to read descriptions to better understand the nature of the outcomes.

#### Responsive Design
- Optimized for various devices, ensuring accessibility and a consistent experience across all screen sizes.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/6127c86b-da16-449f-a7e9-f74dd020ae88)


### Features Left to Implement

#### Resources
- The ability at attach resources, such as scientific papers, research papers, graphs, charts, memos, or anything else that might help collabortors better understand the nature of the hazard or outcome.

#### User Dashboard
- A personalized space for users to track their contributions and receive updates.
- Aims to enhance user engagement and personalize the experience.

#### Advanced Search and Filter
- To provide enhanced search functionality, allowing users to filter content based on specific criteria.

#### Interactive Risk Matrix and Node Graph
- A visual tool for mapping and understanding the interconnections between various hazards.
- Aims to provide a more intuitive way of visualizing risks and their relationships.

#### Versioning
- Implementing version control for user contributions to maintain the integrity of the information.

#### DAG Interdependency
- A visual representation of dependencies and relationships between different hazards and outcomes.

#### Conditional Probabilities
- To offer insights into risks under varying conditions, enhancing the analytical aspect of risk assessment.

#### Composite Probability and Severity Equations
- Advanced tools for calculating and understanding the combined impact of various risks.

These features are designed to augment Causa's capabilities in risk analysis, making it a comprehensive tool for understanding and managing risks in various scenarios.

# Testing

## CRUD Comments -- Hazards
| As a/an    | I want to be able to             | So that I can                                       | Expected Results                                   | Actual Results                                     |
|------------|----------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| User       | add a comment to a specific hazard | share my observations or concerns                    | Comment is added and visible under the hazard      | Passed  <img width="1311" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/70b1f1e0-78d2-401c-93b9-1f988a39edd2"> <img width="505" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/8db08445-33f4-4748-b059-9a7cdf65a474"> <img width="420" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/76cf6121-a8e8-49d2-ab8f-c4cebf8433a4">    |
| User       | view comments on a specific hazard | see what others think or have reported               | All comments on the hazard are visible             |   Passed <img width="471" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/350d9109-3c3a-4b5a-95a4-a6162460c633"> |
| Commenter  | edit my comment on a hazard        | correct errors or add new information                | Comment is updated with new text                   |      Passed <img width="770" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/78f359fd-b506-4560-8a98-67501ed89339"> <img width="513" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/92be9784-c650-460e-b56f-b29477f28650"> |
| Commenter  | delete my comment on a hazard      | remove my input if it is no longer relevant or needed| Comment is removed and no longer visible           |  Passed <img width="1258" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/9da73f9b-72c3-45c2-8f7e-7a310b2bce69"> <img width="1079" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/013d4ac6-2dfe-4ff1-aefc-24888f72a129"> |

## CRUD Comments -- Outcomes
| As a/an    | I want to be able to               | So that I can                                       | Expected Results                                   | Actual Results                                     |
|------------|------------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| User       | add a comment to a specific outcome | provide feedback or share my thoughts                | Comment is added and visible under the outcome     | Passed <img width="1147" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/6627e8fc-8e03-4f8f-bff4-179ac6aedee5"> <img width="1009" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/09b2bbe7-c3d3-486c-99ae-dc937a488cb4"> <img width="523" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/c0d10f0e-9635-4c07-8837-d224c02699b6"> |
| User       | view comments on a specific outcome | understand community reactions or additional insights | All comments on the outcome are visible            | Passed <img width="482" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/c640d987-0dac-4855-81b0-3d405a534010"> |
| Commenter  | edit my comment on an outcome       | update my perspective or information                 | Comment is updated with new text                   | Passed <img width="1208" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/4afdc649-994d-446e-bcaa-80228d38b9d7"> <img width="965" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/a76efbb5-4043-479e-b906-833923056919"> <img width="650" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/b98affe7-635b-44ad-9c3b-4925e5fd8eb7"> |
| Commenter  | delete my comment on an outcome     | remove my remarks if they are outdated or incorrect  | Comment is removed and no longer visible           | Passed <img width="1023" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/78a567fb-b37a-4d7f-98e0-13984a204441"> <img width="915" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/6f568cc5-749a-4e76-b6a9-21898c273836"> |

## User Account Creation and Authentication
| As a/an           | I want to be able to                          | So that I can                                       | Expected Results                                   | Actual Results                                     |
|-------------------|-----------------------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Visitor           | sign up for a new user account                | gain access to posting and commenting features       | User account is created and user can log in        | Passed <img width="582" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/1a4f846c-af19-4f87-bc22-275feac4d059"> <img width="1430" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/5fa13021-f20f-40d1-aa30-0d407884d957">

                                                     |
| Registered User   | log in to my account                          | access my user profile and personalize my experience | User is logged in and directed to profile page     | Passed <img width="418" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/2e9e83fd-1db6-4487-afc1-89c26c4c14d9"> <img width="433" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/89fde9d5-ef33-4876-9fd2-9a745fea5d53"> <img width="1016" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/64473762-babd-422b-8b42-cd1e1ebff663">


                                                     |
| Logged-in User    | log out of my account                         | ensure my account is secure when not in use          | User is logged out and session is ended            | Passed <img width="378" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/93b55959-fdea-4fa5-8e2e-3272aad87972"> <img width="975" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/32743b09-6346-4e07-bd34-0a9194b80bd9">

                                                   |


## Responsive Design

## Browser and Device Compatibility

The site was tested on multiple browsers (Chrome, Firefox, Safari) and devices (desktop, tablet, mobile) to ensure compatibility and responsive design adherence.

## Validator Testing

- **PEP8** Passed PEP8 with no errors
models.py:

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/81722d86-48e2-437c-9410-4d1487c77ca3)

views.py:

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/1c8c8992-a55f-45e5-8677-ccf770775833)

risks_outcomes/urls.py:

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/b6811806-f7a3-4c57-9ec7-d161c69501b1)

- **HTML:** Passed W3C validation with no errors.

- ![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/0e7f2bae-7a81-4be1-8960-ec21aefeb2b7)

- **CSS:** Checked with Jigsaw validator; no errors found.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/5ca448c0-8bf4-4dc2-8665-d7d9ef6cb6a8)


## Unfixed Bugs and Issues
All unfixed bugs and issues are catalogued in the [Kanban board]([url](https://github.com/users/laskinner/projects/6/views/1)).

### Functionality
#### Document management
While document management works fine through the admin portal, documents are buggy and troublesome in the app UI. Document names aren't being displayed, and the download link doesn't fuction. These need to be address and this feature will work.

#### Favicon
Favicon needs to be added to eliminate 404 errors from console, and provide image in browser tab

#### Deleting Comments
The Delete comment functionality currently doesn't work. This is likely due to a routing issue, either with the way the javascript helper in comments.js is constructing the URL, or in the way the urls.py is expecting. This proved to be a very difficult problem to understand. For example, editing comments had a similar issue, and it took roughly 1 working day to fix. After many hours of trying to fix this issue, it had to be left as it is in order to complete the project.

### Styles
#### List view
Currently, the list view could use some attention, specically around the cards.

#### Hazard and Outcome details
Probability needs to better displayed as integars, not floats, and with % signs

#### Edit Button
The edit button for comments lacks styling

## Data
#### Fixtures
The project could use more data via fixtures to display pagination, and enrich the overall look and feel of the site.

Currently 
# Deployment

## Deployment Process

The "Causa" project follows a specific deployment process using GitHub for version control and Heroku for hosting. Here are the steps:

### GitHub Repository Management:

1. Development work is conducted on separate branches.
2. Upon completion, changes are merged into the master branch through pull requests.
3. Changes are reviewed and potentially accepted into the master branch.

### Deployment on Heroku:

1. Access the Heroku dashboard and open the specific app for "Causa".
2. Navigate to the "Deploy" tab within the Heroku app dashboard.
3. Scroll to the "Manual Deploy" section.
4. Ensure the main branch is selected.
5. Click "Deploy Branch" to initiate the deployment process.
6. After deployment, click "Open App" to view the live application.

# Credits

## Content

- The project structure and initial setup were inspired by the Code Institute's template. This provided a solid foundation for project organization and best practices.
- Certain functionalities, particularly in Django, were guided by the Code Institute's Blog Walkthrough Project. This helped in understanding and implementing core features of the application.
- Form validation techniques and implementation strategies were sourced from various YouTube tutorials and Stack Overflow discussions, providing insights into efficient and user-friendly form handling.
- The Django documentation was a crucial resource for understanding the framework's capabilities and applying them effectively.

## Media

- Icons used throughout the site were sourced from Font Awesome, enhancing the visual appeal and user experience.

## Acknowledgements

A special thanks to the online developer community for their invaluable resources and support forums. These platforms provided guidance and solutions to various coding challenges encountered during the project development.

This credits section acknowledges the sources of inspiration, guidance, and media assets used in the project. The intention is to appreciate and give due credit to the creators and maintain transparency about the resources utilized.




