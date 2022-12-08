package com.iter.podelki.microservice;

public class Greeting {

    private final String content;

    Greeting(String content) {
        this.content = content;
    }

    public String getContent() {
        return content;
    }
}
