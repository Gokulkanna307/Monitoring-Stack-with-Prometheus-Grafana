# Flask App Monitoring Stack (Prometheus + Grafana)

This project demonstrates a **simple monitoring setup** for a Flask web application using **Prometheus** and **Grafana**, all running with **Docker Compose**.

---

## 🚀 Overview

The goal of this project is to:

- Deploy a sample **Flask application**
- Expose **custom Prometheus metrics**
- Monitor them using **Prometheus** and visualize in **Grafana**

All components are containerized and orchestrated using Docker Compose.

---

## 🧱 Project Structure

├── app.py
├── requirements.txt
├── docker-compose.yml
├── flask_dashboard.json ← Exported Grafana dashboard
└── README.docx

---

## 🐳 Docker Compose Setup

### **docker-compose.yml**

```yaml
services:
  app:
    build: .
    network_mode: "host"
    command: python app.py

  prometheus:
    image: prom/prometheus:latest
    network_mode: "host"
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"

  grafana:
    image: grafana/grafana:latest
    network_mode: "host"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=
```

---

## ▶️ Run the Stack

```bash
docker-compose up --build -d
docker ps
```

---

## 🌐 Access the Services

Flask App http://localhost:5000
Prometheus http://localhost:9090
Grafana http://localhost:3000

---

## 📊 Grafana Dashboard Setup

1. Open Grafana at http://localhost:3000
2. Add Prometheus as a Data Source
3. Create a new dashboard and add metrics such as: flask_request_count_total
4. Once the dashboard looks good, export it:
   **Dashboard → Settings → JSON Model → Download JSON**

---

## 🧹 Stop and Clean Up

```bash
docker-compose down
docker system prune -a #optional To remove all images and volumes
```

---

## ✅ Summary

**This completes the Flask + Prometheus + Grafana Monitoring Stack! 🎉**
