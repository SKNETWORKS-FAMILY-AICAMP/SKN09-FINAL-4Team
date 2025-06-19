# **SKN09-FINAL-4Team**
> SK네트웍스 Family AI 캠프 9기 4팀 FINAL PROJECT <br>
> 개발기간: 25.04.21 - 25.06.20

<br>
<br>

---
# 📚 Contents

<br>

1. [Introduce Team](#1-Introduce-Team)
2. [Project Overview](#2-Project-Overview)
3. [Technology Stack & Models](#3-Technology-Stack-&-Models)
4. [Key Features](#4-Key-Features)
5. [Model Workflow](#5-Model-Workflow)
6. [Deployment Pipeline](#6-Deployment-Pipeline)
7. [Live Demo](#7-Live-Demo)

<br>
<br>

---

# 1. Introduce Team

#### 💡팀명: PetMind
#### 💡프로젝트명: LLM을 활용한 반려견 상담 챗봇
<br>

##### ⬇️팀원 소개 ⬇️

<table align="center" width="100%">
  <tr>
    <td align="center">
      <a href="https://github.com/ohback"><b>@임수연</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/daainn"><b>@이다인</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/nini12091"><b>@김하늘</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/doyeon158"><b>@김도연</b></a>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="./images/수연.jpg" width="80px" /></td>
    <td align="center"><img src="./images/다인.jpg" width="80px" /></td>
    <td align="center"><img src="C:/Users/Playdata/Downloads/하늘.jpg" width="100px" /></td>
    <td align="center"><img src="./images/도연.jpg" width="100px" /></td>
  </tr>
</table>

<br>

---


# 2. Project Overview

### ✅ 프로젝트 소개
**PetMind**는 반려견의 행동 문제와 일상 궁금증을 상담하는 AI 챗봇으로,
사용자는 반려견의 나이, 견종, 성격 등 프로필을 입력하고 LLM 기반 상담을 통해 **반려견의 특성과 상황에 맞는 맞춤형 조언을 받을 수 있는 서비스입**니다.<br>
행동 문제 분석뿐 아니라, 상담 요약 리포트, 반려견 MBTI, 관련 콘텐츠 추천까지 제공하여 보호자가 반려견을 더 깊이 이해하고 케어할 수 있도록 도우며 **텍스트 입력**과 **이미지 인식**을 통한 상담 데이터를 기반으로 실질적인 행동 개선과 보호자 만족도를 높여 누구보다 반려견을 잘 알고 싶은 보호자에게, PetMind는 가장 가까운 AI 파트너가 되어드립니다.




<br>

### ✅ 프로젝트 필요성

<table align="center">
  <tr>
    <td align="center">
      <img src="./images/필요성1.jpg" width="200">
    </td>
    <td align="center">
      <img src="./images/필요성2.jpg" width="200">
    </td>
  </tr>
</table>

반려동물 가구 수가 꾸준히 증가하면서 오늘 날 4가구 중 1가구는 반려동물을 키우고 있을 정도로 관련 시장이 거대해졌지만 커진 시장만큼 반려동물 문제로 어려움을 겪는 보호자도 함께 늘어나고 있습니다. 이러한 문제는 반려동물의 정서뿐 아니라 보호자의 일상과 관계에도 영향을 미칩니다. <br>
그러나 전문적인 행동 교정은 비용과 접근성의 제약으로 누구나 쉽게 이용하기 어렵고,
정보 검색만으로는 개별 상황에 맞는 해결책을 찾기 어렵습니다.
문제는 명확하지만, 이를 일상적으로 해결해줄 개인화된 상담 시스템은 부족한 실정입니다.
이에 따라, 누구나 쉽게 접근할 수 있는 AI 기반 반려견 상담 서비스의 필요성이 커지고 있습니다.



<br>

### ✅ 프로젝트 목표

- 반려인의 스트레스 감소와 정서적 안정 지원
- 전문 상담 접근성 개선을 통한 돌봄 격차 해소
- 반려견 행동 문제의 신속하고 효과적인 해결
- 반려견 관련 사회적 갈등 및 문제 예방에 기여



<br>

---

# 3. Technology Stack & Models

## ✅ 기술 스택 및 사용한 모델



| **Frontend** | **Backend** | **Model Hosting** | **LLM Model** | **DB**| **Vector DB** | **Deployment** | **Collaboration Tool** |
|--------|--------------|-------------|-------------------|----------------|----------------|----------------|----------------------|
| ![HTML](https://img.shields.io/badge/-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)<br>![CSS](https://img.shields.io/badge/-CSS3-1572B6?style=for-the-badge&logo=css&logoColor=white)<br>![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | ![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)<br> ![Django](https://img.shields.io/badge/-Django-092E20?style=for-the-badge&logo=django&logoColor=white)<br> ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?logo=fastapi&style=for-the-badge&logoColor=white) |![RunPod](https://img.shields.io/badge/-RunPod-5F43DC?style=for-the-badge&logo=runpod&logoColor=white) |![Qwen3](https://img.shields.io/badge/-Qwen3-8A2BE2?style=for-the-badge&logo=qwen3&logoColor=white)<br> ![GPT4o](https://img.shields.io/badge/-GPT4o-412991?style=for-the-badge&logo=openai&logoColor=white)<br>| ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white) | ![FAISS](https://img.shields.io/badge/-FAISS-009999?style=for-the-badge&logo=meta&logoColor=white)<br> ![ChromaDB](https://img.shields.io/badge/-ChromaDB-FC521F?style=for-the-badge&logo=ChromaDB&logo=chromatic&logoColor=white) | ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)<br>![AWSEC2](https://img.shields.io/badge/-AWS%20EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)<br>![AWSs3](https://img.shields.io/badge/-AWS%20S3-FFff0?style=for-the-badge&logo=amazonaws&logoColor=white) | ![Git](https://img.shields.io/badge/-Git-F05032?style=for-the-badge&logo=git&logoColor=white)<br>![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)<br>![Discord](https://img.shields.io/badge/-Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)<br>![Notion](https://img.shields.io/badge/-Notion-000000?style=for-the-badge&logo=notion&logoColor=white) |


<br><br>


---
# 4. Key Features

###  ① 반려견 정보 기반 맞춤형 상담 챗봇 도입

보호자가 입력한 **반려견 프로필 정보**(이름, 견종, 나이, 중성화 여부, 주거 환경 등)를 기반으로 **맞춤형 상담 제공**
- 텍스트 입력 외에도 **이미지 인식 기능**을 통해 다양한 질문에 직관적 응답 제공

### ② 견BTI 성격 검사 도입

 반려견의 성향을 **MBTI 기반으로 유형화**하여 성격형 상담 제공  
- 챗봇 응답 시 해당 **성향 정보를 반영한 맞춤형 프롬프트 적용** 
- 사용자가 성격 검사를 반복할 때마다 GPT-4o가 새로운 질문지를 자동 생성 
    - 항상 똑같은 질문 대신 반려견의 **일상적인 행동에서 쉽게 관찰 가능한 질문**으로 구성

###  ③ 상담 내용 기반 콘텐츠 추천

 **TF-IDF 기반 알고리즘**과 **유사도 분석**을 통한 추천 시스템 구축
- 사용자의 상담 내용을 추출하여 관련 지식 콘텐츠 자동 추천  
- 문제 해결을 위한 학습과 정보 제공을 동시에 유도

### ④ 상담 요약 PDF 리포트 제공

 **상담 레포트를 다운로드 가능한 PDF 형태로 제공**하는 기능
- 원하는 날짜의 상담 내용을 요약하여 GPT-4o가 자동 생성한 리포트 제공  

> 상담 리포트 형식: 상담 요약, 주의사항, 다음 상담 제안까지 포함  

<br><br>

---

# 5. Model Workflow


![image](https://github.com/user-attachments/assets/dad4ec8f-691b-4892-8538-027dcd893fb0)




### ① 모델 선정


| 모델        | 텍스트 전용 모델: Qwen3-8B                                  | 이미지 전용 모델: GPT-4o                                      |
|------------------|-------------------------------------------------------------|------------------------------------------------------------------|
| 개발사           | Alibaba Cloud                                               | OpenAI                                                           |
| 입력값           |텍스트                                           | 이미지 + 텍스트                                       |
| 특징             | 사고 모드(Thinking Mode) 도입으로 복잡한 질문이나 감정 섞인 상담 응답 성능 강화                   | 멀티모달 처리로 맥락 이해력과 의도 파악 정확도가 향상되어, 상담의 공감도와 신뢰도 개선             |


<br>

### ② 의미 기반 검색: RAG + 텍스트 임베딩
- OpenAI의 `text-embedding-3-small` 모델로 문서 임베딩 → FAISS 기반 벡터 검색  
- 다양한 질문 유형에서 안정적이고 높은 일관성의 검색 성능을 기록하여 최종 채택

> 🔗 [임베딩 모델 성능 평가 문서](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-FINAL-4Team/blob/main/documents/8.%20%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%20%ED%95%99%EC%8A%B5%20%EA%B2%B0%EA%B3%BC%EC%84%9C.docx)


### ③ 질문 유형 분류 & 프롬프트 구조 설계

- 사용자의 질문 유형을 `행동 교정 / 정보 탐색 / 감정 공감` 3가지로 분류하여 질문 분류 모델 도입
- 각 유형별 프롬프트를 설계하여 일관된 응답 흐름과 상담의 깊이 확보

### ④ 장기기억 구조 설계
- Qwen3-8B로 최근 10턴의 대화 요약 후, `Chroma DB`에 사용자 ID 기준으로 기억 저장
- 이후 유사한 질문이 들어올 경우, 기억을 검색해 프롬프트에 삽입하여 응답에 반영

> 빠른 검색과 효율적 관리를 위해, `user_id` 기반으로 기억을 저장하고 검색할 수 있는 구조를 지원하는 ChromaDB를 활용

<br><br>

---

# 6. Deployment Pipeline

![image](https://github.com/user-attachments/assets/6ebbc791-2131-412a-ae14-972d91036fed)


* **Django** 기반 웹 서비스를 **Docker**로 컨테이너화하고, **AWS EC2·S3·RDS**와 연계하여 인프라를 구성하였으며, **LangChain**과 **RunPod AP**I를 통해 RAG 기반 챗봇 응답 제공.

<br><br>

---

# 7. Live Demo

