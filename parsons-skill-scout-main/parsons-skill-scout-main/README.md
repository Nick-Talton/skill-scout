# Parsons Skill Scout

## Start-up

Please note that this Start Up is assuming you are using python 3.11.3 and are in a virtual environment (venv) and have [git](https://git-scm.com/download/win) installed. I used [VSCode](https://code.visualstudio.com/download) as my code editor

In a terminal inside of the folder you wish to store Skill Scout, run: 

```git clone https://github.com/ntalton-parsons/parsons-skill-scout.git```

Git clone should work as long as you have access to the github and link your account when it prompts you so that it can verify you have access to the repo.

Verification error from github (server certificate verification failed):

If you get this error please run this command in a terminal ```git config --global http.sslVerify false```

This command will disable SSL Verification for ALL repositories. If you wish to do it with just a single repository please run ```git config http.sslVerify false``` instead

If this is confusing, here is a video of how to start from VSCode: [Video walkthorugh](https://drive.google.com/file/d/1kqsz8PbZqEY7yfKYZGt9yhzE0w4WP3oy/view?usp=sharing)

```pip install -r requirements.txt```

If you run into errors about unable to build wheel that likely means your C++ Build tools is out dated. You need to have at least version 14.00+ installed. ![MS Build tools example](image.png) [Install a newer version here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

In addition to this for the spaCy module you must also do something in addition to the requirements.txt file:

You must also run in the terminal ```python -m spacy download en_core_web_sm``` and ```python -m spacy download en_core_web_lg``` (Please note that you may need version 2.3.1 but it may be possible to run on 2.2.1)

Next, open a python terminal (you can make a python file if you would like but you can just type ```python``` in your terminal):

Then you will want to type 2 lines of code:

```import nltk```

```nltk.download('stopwords')```

If you are in terminal you will not need to run it but if you made a file go ahead and run that file.

If you are in terminal type ```exit()``` to leave the python terminal and return to your localhost.

Skill Scout should be good to run now! 

In the folder with manage.py run: ```python manage.py runserver```

## Contributors

**Nicholas Talton**  
Email: nicholas.talton@parsons.com / nrt3xs@virginia.edu  
Role: Summer 2023 Software and Database Engineering Intern

LinkedIn: [Nicholas Talton LinkedIn](https://www.linkedin.com/in/nicholas-talton-a01289234/)

Nicholas Talton is a talented Software and Database Engineering intern who played a crucial role in developing the Skill Scout project during his Summer 2023 internship and Winter follow up at Parsons. His dedication and expertise in full-stack web development using Django, data management with MySQL and SQLite, and Natural Language Processing (NLP) techniques significantly contributed to the project's success. Nicholas's ability to efficiently analyze and extract data from Excel spreadsheets and Word documents streamlined the candidate matching process, saving valuable time for recruiters and hiring managers.

## Description
Parsons Job Bot is a cutting-edge, full-stack web application developed using the Django framework, designed to revolutionize the candidate matching process for recruiters and hiring managers. As the lead developer, I spearheaded the entire project from concept to implementation, leveraging Django's robust capabilities to create a seamless user experience.

## Key Features and Achievements

### Excel Spreadsheet Data Ingestion
Skill Scout's first groundbreaking feature is its ability to ingest data from Excel spreadsheets and automatically convert it into structured objects stored in a MySQL backend. This streamlined data entry process significantly reduced administrative overhead and improved data accuracy.

### PDF/Word Document Table Scanning
I implemented a powerful PDF and Word document processing module that intelligently scanned and extracted tables containing job positions mentioned in the Excel spreadsheet. This feature saved countless hours for users by automating the previously manual task of extracting job details.

### Natural Language Processing (NLP) for Resume Parsing
Employing advanced NLP techniques, Skill Scout effortlessly extracted vital candidate information, such as skills, name, education, and more, from submitted resumes. The system's ability to understand and interpret natural language elevated the user experience to new heights.

### Intelligent Candidate-Skill Matching
One of the project's core functionalities was to match candidates with open job positions efficiently. Upon clicking on a candidate's profile, Skill Scout dynamically compared their skills with the job descriptions, utilizing NLP to understand context and relevancy. This process generated a unique similarity score for each open position, enabling recruiters to pinpoint the best-suited candidates quickly.

## Technologies and Tools

- Django framework for rapid web application development.
- SQLite for efficient data storage and retrieval.
- Python's powerful NLP libraries, including NLTK and spaCy, for text analysis and understanding.
- PyPDF2 and python-docx for processing PDF and Word documents.

## Impact and Results

Skill Scout transformed the traditional candidate screening and matching process, leading to impressive outcomes:

- Reduced candidate search time through automated resume parsing and skill extraction.
- Can Increase recruiter productivity by automating the comparison of candidate skills with job requirements.

## Skills Demonstrated

- Full-stack web development using Django framework.
- Data ingestion and management with SQLite.
- Natural Language Processing (NLP) techniques for intelligent text analysis.
- PDF and Word document processing and extraction.
- Project management and team coordination.

## Future Development

Continuously striving for improvement, I plan to expand Skill Scout's capabilities by integrating machine learning algorithms to enhance candidate-job matching accuracy. Additionally, I aim to introduce a user-friendly dashboard for visualizing hiring trends and statistics, further empowering recruiters to make data-driven decisions. Additionally I am working on making a forecasting "What if?" Job filling where you can pick a candidate and a job and then backfill the previous position that is now vacant with people from that candidate's team.

Skill Scout remains an ongoing project, and I am excited to continue evolving it to meet the ever-changing needs of the hiring landscape.
