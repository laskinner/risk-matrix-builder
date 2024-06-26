# Causa -- A Risk Management Tool

Causa is a Django-based web application focused on identifying, cataloging, and mitigating various hazards and their associated outcomes. Designed for risk management professionals operating in high-stakes enivornemnts, such as human space flight, Causa offers a platform to catalog and discuss potential risks in various outcomes. The best way to use Causa is to delpoy the repo, deploy, and begin adding hazards and outcomes on the appropriate subject matter. Admins can contribute by adding hazards, detailing their probability and severity, and suggesting potential outcomes. The community aspect of Causa allows for a collaborative approach, where users can comment on and discuss each hazard, providing insights and solutions. This interactive environment makes Causa not just a risk assessment tool, but also a hub for learning and sharing knowledge about risk management in a dynamic, user-friendly interface.


![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/e751150a-d257-4f6d-bc04-5dbdad68ca45)

[Link to livesite](https://django-luke-blog-2de7d643cd1a.herokuapp.com/)


# Causa Project Readme

## Features

### Existing Features

#### Navigation Bar
- Featured across all pages for easy and consistent navigation.
- Enhances user experience by allowing seamless access to various sections of the site.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/62245308-6c08-4340-ab1b-1cf549bfc341)



#### Hazard and Outcome Lists
- Displays user-contributed hazards and outcomes in an organized manner.
- Aids users in quickly identifying and accessing specific risks and their details.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/46405ae6-2f66-4816-80f0-ae291131f5d5)


Both the Hazard and Outcome List views are based upon the following mock-up:
![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/b8a808b6-a776-45ed-a03c-8e766dad1870)


#### Hazard and Outcome Detail Pages
- Provides comprehensive information about each hazard and outcome.
- Includes user comments and discussions, fostering a community-focused environment.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/66fc84e7-ec5a-48ef-9926-2c35007343dd)


Both and Hazard and Outcome Detail pages are bosed upon the following mock-up:
![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/f5bb5d2c-06f9-494e-b55f-b0c251f9d370)



#### Comment System
- Engages users by allowing them to share insights and experiences related to various hazards and outcomes.
- Strengthens the community aspect of the platform.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/e5119a05-813b-4cae-a70f-faf33106b13f)



#### User Authentication
- Ensures a secure and personalized user experience.
- Allows users to contribute and interact with content based on their interests and expertise.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/6cd23897-3e16-4672-b6b3-bb4d04d8959d)


#### Document Management
- Allows admins to upload supporting documents, such as scientific papers or research, to specific hazards and outcomes.
- Allows users to download supporting documents through the UI.

#### Description
- Allows admins to create valuable descriptions for hazards and outcomes.
- Allows users to read descriptions to better understand the nature of the outcomes.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/c6a582d5-037b-466e-ae32-2074c9cdad0e)


#### Responsive Design
- Optimized for various devices, ensuring accessibility and a consistent experience across all screen sizes.

![image](https://github.com/laskinner/risk-matrix-builder/assets/1858258/9b4a3ee2-d07c-4e06-923a-89fc610f0eb1)


### Features Left to Implement

#### Resources and Documents
- The ability at attach resources, such as scientific papers, research papers, graphs, charts, memos, or anything else that might help collabortors better understand the nature of the hazard or outcome.

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/9)

#### Interactive Risk Matrix and Node Graph
- A visual tool for mapping and understanding the interconnections between various hazards.
- Aims to provide a more intuitive way of visualizing risks and their relationships.

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/11)

#### Versioning
- Implementing version control for user contributions to maintain the integrity of the information.

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/13)

#### Markdown Editor for description

- To allow for better user experience, a full feature markdown editor for descriptions would be a great UX improvement.

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/19)

# Testing

## CRUD Comments -- Hazards

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/36)

| As a/an    | I want to be able to             | So that I can                                       | Expected Results                                   | Actual Results                                     |
|------------|----------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| User       | add a comment to a specific hazard | share my observations or concerns                    | Comment is added and visible under the hazard      | Passed  <img width="1311" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/70b1f1e0-78d2-401c-93b9-1f988a39edd2"> <img width="505" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/8db08445-33f4-4748-b059-9a7cdf65a474"> <img width="420" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/76cf6121-a8e8-49d2-ab8f-c4cebf8433a4">    |
| User       | view comments on a specific hazard | see what others think or have reported               | All comments on the hazard are visible             |   Passed <img width="471" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/350d9109-3c3a-4b5a-95a4-a6162460c633"> |
| Commenter  | edit my comment on a hazard        | correct errors or add new information                | Comment is updated with new text                   |      Passed <img width="770" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/78f359fd-b506-4560-8a98-67501ed89339"> <img width="513" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/92be9784-c650-460e-b56f-b29477f28650"> |
| Commenter  | delete my comment on a hazard      | remove my input if it is no longer relevant or needed| Comment is removed and no longer visible           |  Passed <img width="1258" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/9da73f9b-72c3-45c2-8f7e-7a310b2bce69"> <img width="1079" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/013d4ac6-2dfe-4ff1-aefc-24888f72a129"> |

## CRUD Comments -- Outcomes

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/37)
| As a/an    | I want to be able to               | So that I can                                       | Expected Results                                   | Actual Results                                     |
|------------|------------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| User       | add a comment to a specific outcome | provide feedback or share my thoughts                | Comment is added and visible under the outcome     | Passed <img width="1147" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/6627e8fc-8e03-4f8f-bff4-179ac6aedee5"> <img width="1009" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/09b2bbe7-c3d3-486c-99ae-dc937a488cb4"> <img width="523" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/c0d10f0e-9635-4c07-8837-d224c02699b6"> |
| User       | view comments on a specific outcome | understand community reactions or additional insights | All comments on the outcome are visible            | Passed <img width="482" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/c640d987-0dac-4855-81b0-3d405a534010"> |
| Commenter  | edit my comment on an outcome       | update my perspective or information                 | Comment is updated with new text                   | Passed <img width="1208" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/4afdc649-994d-446e-bcaa-80228d38b9d7"> <img width="965" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/a76efbb5-4043-479e-b906-833923056919"> <img width="650" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/b98affe7-635b-44ad-9c3b-4925e5fd8eb7"> |
| Commenter  | delete my comment on an outcome     | remove my remarks if they are outdated or incorrect  | Comment is removed and no longer visible           | Passed <img width="1023" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/78a567fb-b37a-4d7f-98e0-13984a204441"> <img width="915" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/6f568cc5-749a-4e76-b6a9-21898c273836"> |

## User Account Creation and Authentication

[Link to issue](https://github.com/laskinner/risk-matrix-builder/issues/38)
| As a/an           | I want to be able to                          | So that I can                                       | Expected Results                                   | Actual Results                                     |
|-------------------|-----------------------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Visitor           | sign up for a new user account                | gain access to posting and commenting features       | User account is created and user can log in        | Passed <img width="582" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/1a4f846c-af19-4f87-bc22-275feac4d059"> <img width="1430" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/5fa13021-f20f-40d1-aa30-0d407884d957"> |
| Registered User   | log in to my account                          | access my user profile and personalize my experience | User is logged in and directed to profile page     | Passed <img width="418" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/2e9e83fd-1db6-4487-afc1-89c26c4c14d9"> <img width="433" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/89fde9d5-ef33-4876-9fd2-9a745fea5d53"> <img width="1016" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/64473762-babd-422b-8b42-cd1e1ebff663"> |
| Logged-in User    | log out of my account                         | ensure my account is secure when not in use          | User is logged out and session is ended            | Passed <img width="378" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/93b55959-fdea-4fa5-8e2e-3272aad87972"> <img width="975" alt="image" src="https://github.com/laskinner/risk-matrix-builder/assets/1858258/32743b09-6346-4e07-bd34-0a9194b80bd9"> |

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
### Documents and Resources
The primary bug which remains to be fixed is with regards to document upload. To complete this feature, a user also needs to be able to download the documents attached by the admin, which a user can not do. This bug and it's specific usability issues are document in issue [#15](https://github.com/laskinner/risk-matrix-builder/issues/15).

### Editing Hazards and Outcomes in Production
After much investigation, a cause was never discovered for this issue. However, editing the same hazards and outcomes on a local deploy works fine, therefore this issue isn't a show-stopper. It occurs when attempting to edit a hazard or outcome in the admin dashboard, but only in a production environment. It's possible to edit them locally, therefore the site is still usable. To edit a hazard or outcome, simply run "python3 manage.py runserver", and navigate to the admin Dashboard. This bug is reported in issue [#39](https://github.com/laskinner/risk-matrix-builder/issues/39).

### General Styling
The site could use a dark mode styling addition, which would add to the sites general UX. The decision was made not do this at this juncture not to incorporate dark mode, as getting the site across the finish line was the main priority, and introducing dark mode would likely require a long period of debugging. However, a color pallette was determined and documented in the styling updates issue, which is now close. This was document in issue [#32](https://github.com/laskinner/risk-matrix-builder/issues/32).

### Favicon
Favicon needs to be added to eliminate 404 errors from console, which can be found in [#40](https://github.com/laskinner/risk-matrix-builder/issues/40).

Currently 
# Deployment

## Deployment Process

The "Causa" project follows a specific deployment process using GitHub for version control and Heroku for hosting. Here are the steps:

### GitHub Repository Management:

1. Development work is conducted on separate branches.
2. Upon completion, changes are merged into the master branch through pull requests.
3. Changes are reviewed and potentially accepted into the master branch.

### Deployment:

It is recommended to begin with a clean database to begin cataloguing new risks and hazards. To do so, use a SQL provider. This reposotiry uses [ElephantSQL]([url](https://www.elephantsql.com/)).

This project was deployed using Heroku, however any hosting provider compatible with SQL and Django will work.

To depoy:
1. Fork this respository using Github or another version contral manager.
2. Be sure to adjust Settings.py to utiliize env.py, SECRET_KEY, and your hosting provider is added to allowed hosts.
3. Add the SECRET_KEY and DATABE_URL in env.py
4. Add env.py to .gitignore
5. Crete a Procfile and declare this to be a webprocess.
6. Collect the static files by running collectstatic.
7. Push code to Github or a version control manager of your choice.
8. Create the app on your hosting provider, add the DATABASE_URL and SECRET_KEY, and connect it it the repo.
9. Deploy code, and begin using.

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




