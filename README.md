This project demonstrates a local monitoring stack using Prometheus and Grafana to monitor a sample Flask application.

The project contains a Flask app that exposes custom metrics, a Prometheus configuration to scrape those metrics, and Grafana dashboards to visualize them.

To run the project, you need Docker, Docker Compose, and Git installed on your machine.

First, clone the repository from GitHub and navigate to the project directory.

Start all the services by running Docker Compose with the build option to ensure fresh images, and in detached mode so containers run in the background.

You can verify that the containers are running by listing all active Docker containers.

The Flask application is available on port 5000, Prometheus on port 9090, and Grafana on port 4000.

The default credentials for Grafana are username "admin" and password "admin".

To create a new dashboard in Grafana, open Grafana in a browser, log in, and then select "Create → Dashboard → Add new panel".

Choose Prometheus as the data source, enter your custom metric queries, select the type of visualization you want (like graphs or tables), and save the panel.

You can export dashboards by opening the dashboard settings, choosing the JSON model, and saving the file into the dashboards folder.

To stop all running containers, use Docker Compose down. To stop a specific container, use Docker stop followed by the container name or ID.

Make sure no other applications are using the ports 5000, 9090, or 4000 to avoid conflicts.

The Flask app exposes metrics at the /metrics endpoint, which Prometheus scrapes for monitoring.
