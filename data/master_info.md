# Master Info – Erfan Afshar


## Summary

Recent graduate in Computer Engineering (Master, thesis-based) from Concordia University. Thesis focused on anomaly detection on drones using their sensor and actuator data. Developed novel machine learning algorithms for anomaly detection.

7 years of programming experience with a variety of languages in academic settings. 5 years of machine learning learning and development. Proficient in different aspects of machine learning from dataset generation and preprocessing to model development and deployment. Expertise in RNNs. Interested in applying AI solutions to real-world problems.

Able to work as a software developer due to having experience in a variety of programming languages. Great candidate for machine learning model development with proficiency in Python and SQL. Experienced in ML frameworks such as TensorFlow, PyTorch, Scikit-learn, Pandas.

Great at teamwork and independent work based on previous experiences. Many projects with C and Java. Have worked on full stack websites such as e-commerce.

**Keywords**: Computer Engineering, Machine Learning, Python, SQL, TensorFlow, RNN, AI, Anomaly Detection, Software Development, Full Stack, C, Java, PyTorch, Scikit-learn, Pandas


## Education

### Master of Applied Science – Computer Engineering  
**Concordia University**
Thesis-based program focused on anomaly detection using ML and control systems for autonomous drones.  
Key Courses: Optimization, Neural Networks, Multi-Agent Control, Linear Systems Control

### Bachelor of Science – Computer Engineering  
**Amirkabir University of Technology (Tehran Polytechnic)**  
Completed a wide-ranging program covering both software and hardware engineering topics.

**Courses**:
- **Core Computer Science & Programming**:  
  - Principles of Computer & Programming (with Lab)  
  - Advanced Programming (with Lab)  
  - Data Structures and Algorithms  
  - Algorithm Design  
  - Programming Languages

- **Systems & Architecture**:  
  - Operating Systems (with Lab)  
  - Computer Architecture (with Lab)  
  - Microprocessor and Assembly Language (with Lab)  
  - Embedded and Real-Time Systems  
  - Multicore Programming

- **AI & Data Science**:  
  - Principles & Applications of Artificial Intelligence  
  - Principles of Computational Intelligence  
  - Data Mining  
  - Information Retrieval

- **Software & Web Development**:  
  - Software Engineering I  
  - Web Programming  
  - Principles of Database Design (with Lab)

- **Math & Theoretical Foundations**:  
  - Discrete Mathematics  
  - Logic Circuits (with Lab)  
  - Principles of Compiler Design

- **Networking & Communications**:  
  - Computer Networks (with Lab)  
  - Data Communications

- **Additional Topics**:  
  - Electrical and Electronic Circuits (with Lab)  
  - Research and Technical Presentation  
  - Principles of Cloud Computing


## Work Experience

### Data Analyst  
**TELUS Digital AI Data Solution**  

Focused on evaluating and improving AI-generated content, with emphasis on web search relevance, generative AI quality, and data validation.

Analyzed and rated web search results for relevance, language quality, and alignment with user intent to refine search engine performance.

Evaluated generative AI outputs (voice and text) by providing detailed quality assessments and actionable improvement suggestions.

Cross-checked AI-generated content for factual accuracy using trusted external sources across multiple domains.

Completed specialized evaluation tasks, including visual content verification, intent classification, and color-based image analysis.

**Keywords**: AI Evaluation, Search Relevance, Generative AI, Quality Assessment, Data Annotation, NLP, Voice Analysis, Content Validation, Information Retrieval


### AI Automation Specialist  
**CLT Solutions**  

Developed AI-powered voice automation systems for restaurants using N8N, Twilio, and OpenAI, enhancing customer experience and reducing manual workload.

Designed and deployed an AI voice assistant with Twilio and OpenAI to handle restaurant orders through natural, real-time phone conversations.

Automated end-to-end workflows for call handling, order logging, and customer data collection using N8N and third-party integrations.

Implemented fallback mechanisms for ambiguous AI responses, including escalation flows and human handoff options.

Built personalized experiences for repeat customers using dynamic workflows that suggest past orders and respond contextually.

**Keywords**: N8N, Twilio, OpenAI API, Voice Automation, Zapier, NLP, Workflow Automation, AI Assistant, Customer Interaction, Integration Design


### Research Assistant  
**Concordia University**

#### Research focused 

Independently defined tasks, structured workflows, and delivered results on time. Completed the program 10 months ahead of the average master's student under the same supervisor.

Effectively communicated and collaborated with a research group of 15 members by presenting research findings in weekly meetings. Constructive feedback was provided to refine work, and insightful evaluations were shared to improve peers' projects. Analyzed and evaluated over 50 research works to identify gaps in the literature, allowing the development of solutions tailored to under-explored areas.

Demonstrated strong self-management by staying motivated throughout the master's program despite a multitude of problems and maintained consistent weekly efforts of 30–40 hours. Wrote a technical and detail-oriented report of over 130 pages with full coherence and logical flow. Provided and presented convincing presentations.

Developed two novel ML models to improve performance. Conducted full research on the whole area of machine learning to gather ideas and propose a novel solution in an active research area. Searched thoroughly through all recent works on anomaly detection for drones and identified weak points in other works. The MO model provides detection, identification, and isolation of cyber-attacks using a single ML model. The MIMO model performs detection, identification, and isolation of cyber-attacks for a network of drones by processing each drone's data independently, then extracting shared patterns using a single LSTM backbone.

Understood the quadcopter mathematical model. Implemented the quadcopter model in MATLAB and tested it to ensure correctness. Developed both linear and nonlinear models. Designed a controller for the linear system using a combination of single and cascaded PID controllers. Applied the same controller to the nonlinear model, achieving local controllability.

Applied cyber-attacks on the quadcopter during its movement. Types of cyber-attacks included DoS, FDI, and Replay. For DoS, the previous value is repeated for C&C. For FDI, a false value is injected into the communication network. For Replay, a false actuator command is injected while sensor values are replayed from previously recorded data.

Evaluated the cyber resilience of the quadcopter by applying attacks and providing ML solutions to effectively detect, identify, and isolate them. Applied broad ML knowledge to a specific use-case of detecting cyber-attacks on drones using their sensor and actuator data. Highlighted that the same knowledge could be applied to detect attacks on computer networks using ML as well.

**Keywords**: Research, Machine Learning, Anomaly Detection, RNN, LSTM, TensorFlow, MATLAB, Simulink, PID Control, Cybersecurity, Quadcopter Modeling, Drone Systems, Multi-Agent Systems, Time-Series Data, Self-Management, Presentation Skills, Literature Review, Technical Writing


#### implementation focused

Led the full ML pipeline, from problem definition to evaluation. Designed and implemented data generation, modeling, and ML model development to solve real-world challenges. Designed and implemented two innovative LSTM-based frameworks: MO and MIMO.

The MO model provides detection, identification, and isolation of cyber-attacks on a single drone using an end-to-end LSTM architecture. The MIMO model is capable of processing data from multiple drones independently and identifying shared patterns using a unified LSTM backbone. These models offer a significant step forward in autonomous cybersecurity.

Models achieved a 12% improvement in F1-score compared to similar works. Generated two datasets with 50,000 entries each — one with 10 features and the other with 50 features — capturing different dimensions of drone sensor and actuator data.

Data was generated by modeling, controlling, and simulating cyber-attacks on drones using MATLAB and Simulink, then exported to MATLAB for organization and CSV conversion. Applied three types of cyber-attacks: False Data Injection (FDI), Replay Attacks, and Denial of Service (DoS). FDI injects false values into the communication network; Replay reuses previously recorded sensor values while modifying actuator commands; DoS freezes commands by repeating the last control input.

Developed a mathematical model of a quadcopter using both linear and nonlinear systems. Designed and applied PID controllers — both single and cascaded — to stabilize drone control under normal and attack scenarios. Adapted the same controller to the nonlinear model and verified local controllability through simulation.

Reviewed the full landscape of research in drone security and time-series ML methods. Focused on RNNs due to their importance in handling time-series data. Searched all recent anomaly detection works for drone systems and highlighted weaknesses in their approaches.

Delivered strong visual presentations of the work with supporting diagrams, and prepared a comprehensive technical report exceeding 130 pages, including all background research, methodology, results, and discussion. Extended the research to multi-agent drone systems, improving scalability and system complexity. Developed and tested new ML models for detecting network-level attacks in distributed drone swarms. Tuned multiple hyperparameters and tested performance under different attack scenarios.

This use-case shows how ML models trained on actuator and sensor data can effectively secure drones — and demonstrates the potential for reuse in broader cybersecurity applications such as computer network attack detection.

**Keywords**: Anomaly Detection, Cybersecurity, Drone Systems, RNN, LSTM, TensorFlow, MATLAB, Simulink, Time-Series Data, PID Control, MO Model, MIMO Model, Multi-Agent Systems, False Data Injection, Replay Attack, DoS, Dataset Generation, System Modeling, ML Pipeline, Hyperparameter Tuning, Research Presentation, Technical Writing


#### LLM extentsion

Developed an LLM-powered information extraction system to make the 140-page thesis more accessible and searchable for diverse users.

Built a local Python-based application that loads the thesis, segments it into semantically meaningful chunks, and embeds them using transformer-based models.

Integrated a retrieval-augmented generation (RAG) pipeline that allows users to ask natural-language questions and receive accurate, context-aware answers.

Designed prompt templates for multiple use cases, including open-ended Q&A, section-level summarization, and follow-up question generation.

Ensured a low-cost, self-contained setup using FAISS for local vector search and OpenAI’s GPT-4 API for high-quality responses.

Planned future extension of the system with a simple Streamlit interface to allow users to explore thesis content through guided Q&A or structured topic selection.

The tool demonstrates the practical application of GenAI to personalize, summarize, and navigate domain-specific research documents.

**Keywords**: LLM, OpenAI API, GPT-4, Retrieval-Augmented Generation, FAISS, Semantic Search, Prompt Engineering, Document Understanding, Thesis QA System, Python, Streamlit, Information Extraction, Academic NLP, Vector Embeddings



### Machine Learning Intern 
**Amerandish**

Built supervised machine learning models for classification and regression tasks to predict user behavior, achieving a 10% improvement in accuracy over state-of-the-art models. Utilized Python with libraries such as Scikit-learn, TensorFlow, and Pandas to implement and evaluate models.

Applied CNNs for image-based object classification and RNNs for time-series forecasting, reaching up to 85% accuracy. Reduced preprocessing time by 30% through data cleaning pipelines.

Integrated model outputs into dashboards to support internal business decisions, enabling data-driven workflows across teams.

Built a preprocessing pipeline to clean, normalize, and transform user data from web activity logs (100K records) for ML readiness.

Trained and fine-tuned ML models using Scikit-learn and TensorFlow to predict user behavior patterns with up to 90 percent accuracy.

Evaluated and compared model performance using accuracy and runtime to select the most effective solution.

**Keywords (ML)**: Python, TensorFlow, Scikit-learn, CNN, RNN, Time-Series, Model Training, Data Cleaning, Data Analysis, ML Evaluation



### Software Engineering Intern 
**Qeshm Voltage**


Contributed to internal backend development by integrating ML model outputs into Java-based microservices and REST APIs.

Built data handling utilities and lightweight backend endpoints using Java and Python. Supported internal teams by making model predictions available to dashboards and internal tools.

Gained experience in software architecture, service integration, and backend development workflows as part of a cross-functional engineering team.

Developed Java-based REST APIs and microservices to automate workflows for robotic arm control, improving system responsiveness and maintainability.

Integrated low-level C/C++ modules with Java services to enable real-time data exchange with industrial sensors and actuators.

Contributed to a cross-functional engineering team by delivering scalable Java backend solutions that boosted automation reliability by 30 percent.

**Keywords (SWE)**: Java, Python, REST APIs, Backend Development, Software Engineering, Microservices, Data Integration, Internal Tools, C, C++


### Crew Member  
**McDonald’s**

Worked under pressure and stress. Effectively finished jobs under pressure and showed resilience.

Communicated effectively with colleagues as well as managers to maintain a good and healthy team environment. Had excellent teamwork experience in a multinational environment.

Communicated with customers to satisfy them with their orders, especially on special/customized requests. Worked hard toward customer satisfaction even in hard times.

Recognized as a good employee who was willing to do his best for the company’s success. Demonstrated adaptability in the work environment due to a variety of issues, such as broken devices or introduction of new sandwiches.

**Keywords**: Customer Service, Teamwork, Communication, Resilience, Fast-Paced Environment, Adaptability, Multinational Collaboration, Conflict Resolution, Problem Solving


### Delivery Partner  
**Independent / App-Based Platform**

Showed strong self-management and motivation by doing delivery on foot every single day of the week, including on Christmas Day.

Demonstrated patience while waiting in restaurants when they needed more time to prepare orders. Maintained motivation and resilience even when the Uber app created obstacles, such as not assigning deliveries, which were intended to discourage continued work.

Displayed kindness and understanding toward customers in various challenging situations, including broken buzzers, incorrect addresses, or delivery delays — resulting in a 98% satisfaction rate.

Showed resilience in a competitive environment where anyone could work, and was able to consistently earn around $1,000 per month.

**Keywords**: Self-Management, Motivation, Resilience, Customer Satisfaction, Patience, Delivery, Independent Work, Problem Solving, Communication, Competitive Environment



## Projects

### Project: AI Voice Agent for Restaurant Call Automation

**GitHub**: https://github.com/Erfanafshar/restaurant-call-automation

Designed an AI-powered voice automation system to handle customer phone calls for a local restaurant, particularly during peak hours when staff are unavailable.  

Built a two-phase system using OpenAI, Twilio, and N8N to either capture missed calls and follow up, or directly process spoken food orders through a voice assistant.

In the first phase, implemented call capture and callback workflows using Twilio and N8N, enabling customers to leave voice messages or request a callback.  

Integrated follow-up logic that checks if the customer exists in the database and triggers SMS/email confirmations, personalized order summaries, or staff escalation if needed.

In the second phase, developed a conversational AI voice agent capable of understanding natural language, taking full food orders, confirming details, and logging them in a backend system.  

Included features like caller recognition, order prediction for repeat customers, and optional follow-ups via SMS/email using third-party APIs.

Planned future extension to provide cost estimation and dynamic menu support, while ensuring fallback mechanisms for unclear orders or human intervention when needed.

**Keywords**: LLM, Voice Assistant, Twilio, N8N, OpenAI API, Restaurant Automation, Workflow Design, Conversational AI, Order Processing, SMS Integration, Email Automati


### Project: Resume Tailor – LLM-Guided LaTeX Resume Customizer

**GitHub**: https://github.com/Erfanafshar/resume-tailoring-automation

Developed a semi-automated resume customization tool that uses LLMs to rewrite LaTeX-based resumes section by section based on a job description.  

Built the system to accept a LaTeX resume file, a personal information document, and a pasted job ad, then generate tailored suggestions for each section (e.g., summary, experience, projects).  

Enabled interactive approval: the user can review each LLM-generated suggestion before the system replaces the original section in the LaTeX source file.  

Engineered the prompt flow to identify matching resume sections, rewrite them with job-aligned language, and preserve formatting and LaTeX syntax.  

Planned future enhancements including PDF auto-compilation, diff previews, and a simple UI for non-technical users.  

The project demonstrates how LLMs can be integrated into document editing workflows to streamline personalized resume generation while retaining control and customization.

**Keywords**: LLM, OpenAI API, LaTeX Automation, Resume Tailoring, Job Matching, Prompt Engineering, Interactive Editing, Text Replacement, Python, Structured Document Processing, Streamlit (Planned), CLI Workflow


### Project: AskSnap – LLM-Based Info Explorer

**GitHub**: https://github.com/Erfanafshar/asksnap-info-extractor

Designed an LLM-powered information assistant that helps users access structured, focused responses without typing long or perfectly worded questions.  

Built the system to support vague or voice-based queries by delivering concise, easy-to-understand output, avoiding long-form text generation.

Implemented structured prompting to extract a 1-line summary and 3–5 bullet points tailored to the topic’s type (e.g., causes, types, solutions, steps).
  
Added a follow-up mechanism where users receive numbered suggestions to continue the conversation without retyping — supporting deeper, broader, or related exploration paths.

Emphasized a low-friction user experience through a Python-based command-line tool, with plans to add a voice-compatible and browser-based version for broader accessibility. 
 
The project demonstrates how LLMs can be used not just for general chat, but to guide users through technical or unfamiliar topics with clarity and minimal effort.

**Keywords**: LLM, GPT-4, OpenAI API, Structured Prompting, Guided Exploration, Voice-Friendly UX, Bullet Summary, Follow-Up Navigation, User-Centered Design, Technical Topics, Python, CLI, Information Simplification


### Project: Face Retrieval Engine

**GitHub**: https://github.com/Erfanafshar/face-Image-retrieval

Produced feature vectors from face images using MTCNN, optimizing data representation. Deployed a vector search engine to identify the most similar images, significantly enhancing search accuracy and efficiency.

Created a face search engine utilizing approximately 750,000 face images, achieving rapid response times for efficient retrieval. The dataset was built using three major sources: CelebA, IMDB-WIKI, and CASIA-WebFace.

Applied MTCNN for face detection across all images. Generated feature vectors using three different embedding techniques: FaceNet, ArcFace, and VGGFace. Performed comparative evaluation of their performance, and computed a weighted combination of all three methods based on empirical results.

Used the Gensim library to build a vector-based search engine for facial similarity retrieval. Designed and implemented the complete backend system in Python, supporting efficient search and data processing for large-scale image data.

Created a full web-based user interface using HTML, CSS, and JavaScript. The system consisted of two main parts: the user interface (frontend) and the machine learning backend. Key system components included: face detection, feature vector generation, and search on feature vectors.

Built frontend features such as dynamic image upload, responsive layout, and search result visualization. Ensured cross-browser compatibility and optimized performance to handle large image datasets. Combined all ML models, embedding logic, and search algorithms into a seamless and efficient end-user experience.

Developed and deployed a complete deep learning–driven image retrieval system, demonstrating proficiency in both backend ML and full-stack integration.

**Keywords**: Face Recognition, Face Retrieval, Deep Learning, MTCNN, FaceNet, ArcFace, VGGFace, Image Processing, Feature Embedding, Gensim, Python, JavaScript, HTML, CSS, Full-Stack, Vector Search Engine, Search Engine Design, Big Data, Dataset Integration


### Project: Hangman Game

**GitHub**: https://github.com/Erfanafshar/hangman-cli-game

Implemented the classic Hangman game logic in C. Designed a user-friendly console-based interface with clear prompts, feedback messages, and progressive visual representation of the Hangman figure.

Developed a word selection mechanism using linked lists. Managed game states, including word guessing, scoring, and user input handling, with error checking and validation for edge cases such as invalid inputs and early exits.

Implemented file handling to store and retrieve words and topics. Enabled a save and resume feature using struct-based data storage, allowing users to pick up previous sessions seamlessly.

Allowed dynamic word list expansion by loading external files into memory. Enabled topic selection so users could choose categories of words for gameplay. Designed a scoring system based on attempts, correct guesses, and penalties for incorrect attempts.

Optimized random word selection to ensure fairness and variation across sessions. Structured code in modular functions, improving readability and maintainability.

Used Git for version control and project management. Ensured clean commit history, backups, and version tracking. Followed best practices in structuring C programs with header files and source files.

**Keywords**: C Programming, Game Development, Linked Lists, Console UI, File Handling, Structs, Data Persistence, Input Validation, Scoring System, Save/Resume Functionality, Modular Design, Git, Version Control


### Project: Normal Tanks Game (Multiplayer Tank Battle Game)

**GitHub**: https://github.com/Erfanafshar/normal-tanks-game

Developed a real-time tank battle game inspired by "Normal Tanks" using Java. Applied Object-Oriented Programming (OOP) principles to design game entities such as tanks, projectiles, enemies, obstacles, and explosions.

Implemented multiplayer functionality, allowing two players to connect and play together over a network. Designed and managed client-server communication using custom networking protocols, handling user inputs and real-time game synchronization.

Created AI-controlled enemies with varying attack patterns and difficulty levels. Handled weapon switching mechanics and implemented keyboard and mouse-based controls for movement, aiming, and firing.

Developed collision detection logic for tank-to-tank, tank-to-environment, and bullet-based interactions. Implemented graphical rendering using Java libraries to create an interactive game world with visual effects.

Built a complete GUI system for the main menu, settings, HUD, and pause screens. Developed a custom map editor that allows players to design and load custom levels. Integrated cheat code functionality for testing and enhanced gameplay features.

Included a difficulty adjustment system, scaling AI behavior and resource availability. Built save/load functionality to allow users to resume progress. Managed concurrency using Java threads to maintain responsive gameplay and background processes.

Optimized performance to ensure smooth rendering and interaction even during intense gameplay sessions. Followed clean coding practices with modular functions and JavaDoc documentation. Used Git and GitLab for version control and team collaboration.

**Keywords**: Java, Game Development, Object-Oriented Programming, Multiplayer Networking, Game Physics, Collision Detection, GUI, Java Threads, File Handling, Custom Map Editor, Save/Load System, Cheat Codes, AI Behavior, Difficulty Scaling, Git, Version Control


### Project: JDM – Java Download Manager

**GitHub**: https://github.com/Erfanafshar/download-manager

Developed a multi-threaded download manager in Java that supports concurrent downloading of multiple files over HTTP and HTTPS protocols. Implemented request handling to fetch files efficiently from servers and handle large file transfers with chunk-based downloading.

Built a user-friendly GUI using Java Swing, including interactive menus, buttons, download lists, and visual progress bars. Designed a dynamic queue system for download task management, allowing users to add, pause, resume, and cancel downloads on demand.

Implemented robust file handling for saving and resuming downloads across sessions. Developed a save state system using data serialization, allowing interrupted downloads to be restored with full progress.

Managed multithreading using Java’s concurrency utilities, ensuring thread-safe operations and responsive user interaction during simultaneous downloads. Configured thread pools and synchronization techniques to balance performance and stability.

Added scheduling features that allowed users to set start times for downloads. Integrated retry logic for failed downloads, and built a notification system for completion and errors.

Enhanced download speeds using multi-segmented file retrieval and optimized bandwidth usage. Included a filtering system that allowed blacklisting of specific websites or file types.

Created configuration settings for download paths, speed limits, UI themes, and user preferences. Ensured security and access control by preventing unauthorized downloads from blocked domains.

Integrated Git for version control and collaboration. Documented codebase using JavaDoc and followed clean, modular design for maintainability.

**Keywords**: Java, Multithreading, Networking, HTTP/HTTPS, Java Swing, GUI Design, File Handling, Download Scheduling, Resume Support, Data Serialization, Retry Logic, Bandwidth Optimization, Concurrency Control, Filtering, Configuration Management, JavaDoc, Git


### Project: Document Retrieval and Ranking System

**GitHub**: https://github.com/Erfanafshar/document-search-engine

Developed an information retrieval system in Java to retrieve and rank documents based on user queries. Handled large-scale text data efficiently using Java’s data structures and multithreading for parallel query handling.

Implemented text tokenization to extract and preprocess words from documents. Applied NLP techniques including stemming and stopword removal to improve search quality. Constructed an inverted index for fast document retrieval and efficient query-time performance.

Designed and implemented the TF-IDF weighting model to calculate term importance across the corpus. Used cosine similarity to measure relevance between user queries and documents. Optimized search efficiency using advanced indexing techniques such as Index Elimination and Champion Lists.

Developed a query processing engine capable of handling both single-word and multi-word searches. Extended the system by incorporating document clustering based on Wikipedia articles, enabling clustering-based query execution to improve retrieval speed and relevance.

Followed structured project development practices and used Git for version control and collaboration.

**Keywords**: Java Programming, Information Retrieval, Search Engine, Text Processing, Tokenization, NLP, TF-IDF, Cosine Similarity, Document Clustering, Multithreading, File Handling, Indexing, Git


### Project: NetWolf – P2P Distributed File Sharing System

**GitHub**: https://github.com/Erfanafshar/netwolf-p2p-fileshare

Developed a peer-to-peer (P2P) file sharing system in Python where nodes can discover, request, and transfer files across a distributed network. Implemented both TCP and UDP socket programming: UDP for peer discovery and TCP for file transfers.

Designed a distributed architecture where each node maintains a dynamic list of active peers in the cluster. Enabled automatic node discovery via periodic UDP broadcast messages, allowing the network to adapt to joining or leaving nodes.

Implemented a file request and response protocol with message serialization/deserialization. Built a priority-based provider selection mechanism, where nodes choose file sources based on latency and response time.

Handled concurrent file transfer requests using multithreading, allowing nodes to serve and request multiple files simultaneously. Designed custom logic for load balancing to prevent a node from being overwhelmed by too many requests.

Integrated timeout handling and retransmission mechanisms to address dropped packets and lost connections. Ensured data consistency and delivery integrity even under unstable network conditions.

Built a command-line interface (CLI) for node control and user interaction. Users could list available peers, request files, view cluster state, and check file availability in real time.

Implemented congestion control to prevent performance degradation. Developed basic security and validation features to prevent malformed requests or unauthorized file access.

Used Git for version control and collaboration. Focused on clean, modular code for maintainability and extensibility.

**Keywords**: Python, Peer-to-Peer Networking, TCP/UDP, Socket Programming, Distributed Systems, Multithreading, File Sharing, Peer Discovery, Latency Optimization, Load Balancing, Timeout Handling, Retransmission, CLI, Custom Protocols, Serialization, Version Control


### Project: E-Commerce Website – Web Programming Project

**GitHub**: https://github.com/Erfanafshar/ecommerce-store

Developed a complete e-commerce website using HTML, CSS, JavaScript (frontend) and PHP, SQL (backend). Designed the site for both functionality and user experience, including user authentication, product browsing, cart management, and checkout processing.

Created a dynamic homepage that displayed rotating promotional banners and product highlights. Implemented user registration and login functionality with session handling and password encryption.

Built a full-featured shopping cart system that allowed users to add and remove products, adjust quantities, and view total costs. Implemented persistent cart storage tied to user sessions, allowing users to resume shopping later.

Designed the backend in PHP to handle product database queries, order processing, and user data management. Used SQL for secure data retrieval and insertion. Ensured robust form validation and error handling across all user interactions.

Developed the admin panel to manage product inventory, add new products, and view user orders. Added filters and search functionality to simplify navigation for users.

Focused on usability and responsive design, ensuring compatibility across different browsers and devices. Styled the frontend using CSS and dynamic DOM manipulation with JavaScript for interactive features such as dropdowns, modals, and real-time cart updates.

Followed modular coding practices, separating presentation, logic, and database access layers. Used Git for version control and progress tracking.

**Keywords**: Web Development, Full-Stack, HTML, CSS, JavaScript, PHP, SQL, E-Commerce, Session Handling, User Authentication, Form Validation, Admin Panel, Cart System, Responsive Design, Frontend/Backend Integration, Git


### Project: Signals and Systems – Audio Signal Processing Project

**GitHub**: https://github.com/Erfanafshar/speech-gender-detection

Implemented a gender classification system using audio signal processing techniques in MATLAB. Developed a script to process MP3 audio files and extract power spectrum data using Fourier Transform (FFT).

Analyzed frequency peaks in recorded speech signals to distinguish between male and female voices. Designed a classification algorithm based on spectral characteristics of human speech and automated batch processing to label multiple audio files.

Researched and implemented Spectral Subtraction for speech enhancement and noise reduction. Added additive white Gaussian noise (AWGN) to test signals and evaluated the effectiveness of the noise reduction process.

Conducted comparative analysis between noisy and enhanced signals, and proposed optimization techniques to improve both gender classification accuracy and noise removal quality.

Compiled a final project report with MATLAB code, experimental analysis, and performance evaluation.

**Keywords**: Signal Processing, Frequency Analysis, Fourier Transform (FFT), Audio Signal Processing, MATLAB, Spectral Subtraction, Speech Enhancement, Noise Reduction, Gender Classification


### Project: Art Gallery Database Management System

**GitHub**: https://github.com/Erfanafshar/picto-db-system

Designed and implemented a relational database system for managing an art gallery using SQL and Python. Modeled the database structure with an Entity-Relationship (ER) diagram that captured relationships between artwork, artists, exhibitions, auctions, and participants.

Created and managed SQL tables with well-defined primary and foreign key constraints to ensure data integrity. Developed full SQL scripts to handle schema creation, data insertion, updates, and deletions.

Built a CRUD-based application that allowed users to manage gallery inventory, track artist contributions, schedule exhibitions, and organize auctions. Implemented auction bid tracking and automatic winner selection based on highest bids.

Designed a user-friendly graphical interface to interact with the backend database, earning bonus credit for GUI integration. Applied business logic such as enforcing minimum pricing constraints and validating auction transactions in real time.

Maintained records of auction participants and linked them to corresponding bids. Generated detailed purchase invoices for successful bidders, including artwork metadata and transaction details.

Submitted a comprehensive project report including ER diagrams, SQL scripts, GUI documentation, and functional evaluation.

**Keywords**: Database Management System (DBMS), SQL, ER Diagram, CRUD Operations, Relational Database, GUI, Transaction Handling, Python, Data Integrity, Auction System


### Project: Cloud Computing – Docker-Based Task Scheduling System

**GitHub**: https://github.com/Erfanafshar/container-scheduler

Developed a container scheduling system for single-node environments using Docker. Deployed and managed Docker containers on an Ubuntu server to execute and distribute user-defined tasks efficiently.

Built a containerized task scheduling engine that handled multiple incoming job requests, using job execution threads to process and assign workloads across running containers. Implemented a CLI-based interface for users to submit jobs and perform different operations such as sorting, word count, and mathematical tasks using containerized scripts.

Configured resource allocation policies for CPU and memory to support optimal load balancing and prevent resource starvation. Designed a multi-container deployment strategy to support parallel task execution while maintaining synchronization between processes.

Automated the request admission pipeline and job execution system to streamline workflow management. Developed a custom Docker image via Dockerfile, including all necessary dependencies and runtime configurations.

Evaluated system performance and applied optimization techniques to improve container utilization and execution efficiency. Documented the full system architecture, including scheduling logic, CLI design, and performance benchmarks, in the final project report.

**Keywords**: Cloud Computing, Docker Containers, Container Scheduling, Ubuntu Server, Virtual Machines (VMs), CLI-based Task Management, Multi-container Deployment, Load Balancing, Resource Allocation, Task Scheduling


### Project: Multi-Node Hadoop Cluster Crime Data Analysis

**GitHub**: https://github.com/Erfanafshar/hadoop-cluster-crime-stats

Designed and implemented a distributed crime data analysis pipeline using a multi-node Hadoop cluster on VirtualBox virtual machines. Built a three-node cluster on Ubuntu (18.04 and 20.04) with one NameNode/ResourceManager and two DataNodes/NodeManagers. Installed Apache Hadoop 3.2.1 and configured HDFS, YARN, and MapReduce for distributed processing.

Established passwordless SSH communication across all nodes. Verified HDFS replication and system stability via CLI and Web GUI. Wrote a custom Java-based MapReduce program to process CSV datasets and count crime incidents per police district.

Downloaded official Chicago crime datasets (2001–2017) from Kaggle, uploaded them to HDFS, and ran the MapReduce pipeline. Output was generated as a CSV summarizing crime count per district (`crime_count_per_district.csv`). Verified all components, including file upload, execution, and result export through command-line tools and HDFS Web UI.

Demonstrated skills in distributed system setup, big data processing, and working with real-world data pipelines using Hadoop ecosystem tools.

**Keywords**: Hadoop, HDFS, YARN, MapReduce, Java, Distributed Systems, Big Data, VirtualBox, Ubuntu, SSH, CSV Processing, Crime Data Analysis, System Simulation


### Project: VirtualBox API Server

**GitHub**: https://github.com/Erfanafshar/virtualbox-api-server

Developed a RESTful API server for remote management of VirtualBox virtual machines. Implemented endpoints for full VM lifecycle control including start, stop, status check, and deletion. Supported VM creation from scratch or cloning existing instances.

Integrated configuration APIs to change CPU and memory allocation dynamically. Enabled remote file operations such as uploading files to a VM and transferring files between VMs. Implemented shell command execution on VMs with response capture.

Built a token-based authentication system to control access levels, enforcing role-based permissions for admin and non-admin users. Used JSON for both request and response formats, ensuring a consistent developer interface.

Tested all functionality with Postman and deployed the API against Ubuntu Server VMs in VirtualBox. Configured networking to support SSH and secure inter-VM communication.

**Keywords**: Python, REST API, VirtualBox, Virtual Machines, HTTP, VM Lifecycle Management, Token Authentication, JSON, SSH, Ubuntu Server, System Automation, File Transfer, Resource Allocation


### Project: Maze Reactive Controller (ROS + Gazebo)

**GitHub**: https://github.com/Erfanafshar/maze-reactive-ros

Designed and implemented a reactive control system for autonomous maze navigation using ROS and Gazebo. Developed two modular ROS nodes — `obstacle-detector` and `velocity-controller` — to handle real-time perception and motion control of a TurtleBot robot.

The system operated without any prior knowledge of the maze layout, relying entirely on live sensor input from a laser scanner and bumper sensors. The `obstacle-detector` node subscribed to sensor topics and published a directional signal when obstacles were detected. The `velocity-controller` node used this feedback to issue velocity commands for continuous, collision-free motion.

Conducted long-duration simulations in the `funky-maze.world` environment. The robot completed multiple loops around the maze over 15+ minute sessions without critical collisions. Demonstrated successful obstacle avoidance and system stability through real-time feedback and simple control logic.

**Keywords**: ROS, Gazebo, TurtleBot, Reactive Control, Obstacle Avoidance, Laser Scanner, Sensor Fusion, Real-Time Systems, Robotics, Python, Autonomous Navigation, Simulation


### Project: E-Commerce SQL Database System

**GitHub**: https://github.com/Erfanafshar/ecommerce-sql-db

Designed and implemented a relational database system for a simplified e-commerce platform. Defined SQL schema for core entities including `Users`, `Products`, `Invoices`, `InvoiceItems`, and `Suppliers`. Built the system to support both transactional operations and analytical queries.

Populated all tables with test data and wrote SQL scripts to support reporting tasks such as filtering users by location, listing products from specific suppliers, computing product ratings, and identifying high-profit items. Implemented update queries to adjust sale prices dynamically and generate summary views for item popularity and supplier contributions.

Developed a Python script to connect to the database using a SQL connector library, enabling programmatic query execution and data extraction for analysis and reporting.

**Keywords**: SQL, PostgreSQL, Relational Database, E-Commerce, Schema Design, Data Modeling, Python Integration, Analytical Queries, SQL Views, Data Insertion, Reporting, Database Systems


### Project: CLI HTTP Client

**GitHub**: https://github.com/Erfanafshar/cli-http-client

Developed a command-line HTTP client from scratch to perform structured HTTP requests with full support for custom headers, query parameters, body payloads, file uploads, and response parsing. Supported HTTP methods include GET, POST, PUT, PATCH, and DELETE.

Implemented robust argument parsing for headers (`--headers`), queries (`--query`), URL validation, and timeouts. Enabled layered overrides for headers and content types, mimicking curl-like behavior while adding structured validation and error handling.

Supported body data in both form-urlencoded (`--data`) and raw JSON (`--json`) formats, with appropriate content-type header management. Added optional support for file uploads via `--file`, and timeout tracking using `--timeout`.

Built a response handler to display status codes, headers, and formatted response bodies. Included optional loading animations and binary-safe response dumps for file content types.

**Keywords**: Python, CLI Tools, HTTP Client, Request Parsing, JSON, File Uploads, Error Handling, Timeout Management, Custom Headers, URL Validation, curl-like Functionality





## Skills

### Programming Languages  
Python, Java, C, C++, JavaScript, MATLAB, Bash, SQL

### Machine Learning & Data Science  
TensorFlow, PyTorch, Scikit-learn, Pandas, NumPy, OpenCV, Matplotlib, Keras, Gensim, Seaborn

### Web Development  
HTML, CSS, JavaScript, PHP, REST APIs, Flask, JSON, AJAX

### Software & Tools  
Git, GitHub, GitLab, Docker, Ubuntu, Windows, VS Code, Eclipse, IntelliJ, Jupyter, Anaconda

### Cloud & DevOps  
Docker, Ubuntu Server, CLI tools, Virtual Machines, Multi-container Systems, Load Balancing

### Databases  
SQL, MySQL, SQLite, PostgreSQL

### Systems & Networking  
Socket Programming (TCP/UDP), Multithreading, File Systems, Command Line Interfaces, Peer-to-Peer Networks

### Control Systems & Simulation  
MATLAB, Simulink, PID Controllers, System Modeling

### Soft Skills  
Teamwork, Self-Motivation, Resilience, Communication, Independent Work, Presentation Skills, Research Skills