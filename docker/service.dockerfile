FROM openjdk:8-jdk-alpine
COPY res/podelki-rest-service-0.1.0.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]