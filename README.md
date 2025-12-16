# 🚀 CI/CD with GitOps

**Project Overview:**  
This project demonstrates a full **CI/CD pipeline** using **Jenkins**, **Kaniko**, **ArgoCD**, and **Kubernetes** on **Minikube**. It automates building, pushing, and deploying a Python Flask application following **GitOps principles**.  

---


## 🛠 Tech Stack

- **CI/CD:** Jenkins, Kaniko  
- **GitOps:** ArgoCD  
- **Container Registry:** DockerHub  
- **Container Orchestration:** Kubernetes (Minikube)  
- **Ingress:** NGINX  
- **Application:** Flask

---

## 🏗 Architecture

![Architecture Diagram](./k8s-cicd/screenshots/architecture.jpg)  
*Flow: GitHub → Jenkins (Kaniko) → DockerHub → ArgoCD → Kubernetes Pods → NGINX Ingress → Browser*

**Flow:**

1. Push code to GitHub
2. Jenkins picks up the commit and builds the Docker image using **Kaniko**
3. Push the image to **DockerHub**
4. **ArgoCD** syncs the deployment manifest from GitHub to the Kubernetes cluster
5. Kubernetes deploys the **Flask app**
6. App is accessible via **NGINX Ingress** at `http://flask.devops.local`

---

## ⚙️ CI/CD Pipeline (Jenkins)

![Jenkins Pipeline](./k8s-cicd/screenshots/jenkins-pipeline.jpg)  
*Pipeline stages: Checkout, Build & Push, Deploy to Kubernetes via ArgoCD*


---

##  Application Deployment

**Kubernetes Resources (Jenkins namespace):**

```bash
kubectl get pods -n jenkins
kubectl get svc -n jenkins
kubectl get ingress -n jenkins
```

---

## ArgoCD Dashboard

Shows the Flask app synced and healthy with automated GitOps deployment.


![Argocd-Dashboard](./k8s-cicd/screenshots/argocd-dashboard.jpg)

![Argocd-Dashboard1](./k8s-cicd/screenshots/argocd-dashboard1.jpg)





