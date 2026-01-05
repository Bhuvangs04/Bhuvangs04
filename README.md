
<div align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=20C20E&width=435&lines=Architecting+Scalable+Microservices;Training+AI+Agents+%26+LLMs;Optimizing+Redis+Caching+Layers;Hello,+I'm+Bhuvan" alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <a href="https://linkedin.com/in/bhuvan-g-sangappanavar-403a022a2">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="mailto:bhuvangs.personal@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://leetcode.com/u/Hackky_Freddy/">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" />
  </a>
</div>

<br/>

### ⚡ Engineered for Scale & Intelligence
* **Core Competency:** Building high-throughput backend systems integrated with Generative AI models.
* **Current Focus:** Optimization of Vector Database retrieval speeds & Redis Pub/Sub architectures.
* **Philosophy:** *"If it's not automated, it's not finished."*

---

### 🏗️ My Hybrid System Architecture
```mermaid
graph TD;
    Client[Client App] -->|Request| LB{Load Balancer};
    LB -->|Route| API[API Gateway / Node.js];
    
    %% Caching Layer
    API -->|1. Check Cache| Redis[Redis Cache Cluster];
    Redis -- Miss --> API;
    Redis -- Hit --> Client;
    
    %% Database Layer
    API -->|2. Query DB| DB[(PostgreSQL / Mongo)];
    
    %% AI Layer
    API -.->|3. AI Inference| AI_Svc[AI Microservice / Python];
    AI_Svc -->|Embeddings| VectorDB[(Vector DB / Pinecone)];
    AI_Svc -->|RAG Context| LLM[LLM Engine];

    style Client fill:#0d1117,stroke:#fff,color:#fff
    style API fill:#0d1117,stroke:#20C20E,stroke-width:2px,color:#fff
    style Redis fill:#201111,stroke:#ff0000,stroke-width:2px,color:#fff
    style AI_Svc fill:#112011,stroke:#20C20E,stroke-dasharray: 5 5,color:#fff

```

### 📊 Engineering Telemetry

| **Automated Data Pipeline** | **Coding Velocity** |
| --- | --- |
| <img src="./chart.png" width="100%" alt="Waiting for Action..." /> | <img src="https://www.google.com/search?q=https://github-readme-stats.vercel.app/api%3Fusername%3DBhuvangs04%26show_icons%3Dtrue%26theme%3Dtokyonight%26hide_border%3Dtrue%26bg_color%3D0d1117%26count_private%3Dtrue" width="100%" /> |
| *Live Python Cron Job (Updates every 6hr)* | *GitHub Contributions Metrics* |

### 🛠 Technical Arsenal

<div align="center">
<table>
<tr>
<td align="center" width="120"><b>Backend</b></td>
<td><img src="https://www.google.com/search?q=https://skillicons.dev/icons%3Fi%3Dnodejs,express,python,django,java,spring,go,graphql%26theme%3Ddark" /></td>
</tr>
<tr>
<td align="center" width="120"><b>Data & Cache</b></td>
<td><img src="https://www.google.com/search?q=https://skillicons.dev/icons%3Fi%3Dredis,mongodb,postgres,mysql,firebase,kafka,elasticsearch%26theme%3Ddark" /></td>
</tr>
<tr>
<td align="center" width="120"><b>AI & ML</b></td>
<td><img src="https://www.google.com/search?q=https://skillicons.dev/icons%3Fi%3Dpytorch,tensorflow,opencv,pandas,sklearn,anaconda%26theme%3Ddark" /></td>
</tr>
<tr>
<td align="center" width="120"><b>DevOps</b></td>
<td><img src="https://www.google.com/search?q=https://skillicons.dev/icons%3Fi%3Ddocker,kubernetes,aws,gcp,git,linux,nginx,jenkins%26theme%3Ddark" /></td>
</tr>
</table>
</div>

### 🐍 Contribution Activity

<div align="center">
<img src="https://github.com/Bhuvangs04/Bhuvangs04/blob/output/github-contribution-grid-snake.svg" width="100%" />
</div>

<div align="center">
<img src="https://www.google.com/search?q=https://komarev.com/ghpvc/%3Fusername%3DBhuvangs04%26style%3Dflat-square%26color%3D20C20E" alt="Profile Views" />
</div>

