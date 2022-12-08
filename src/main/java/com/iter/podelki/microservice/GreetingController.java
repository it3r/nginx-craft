package com.iter.podelki.microservice;

import java.net.InetAddress;
import java.net.UnknownHostException;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    private static final String template = "%s, %s!";

    @RequestMapping("/{path}")
    public Greeting greeting(@PathVariable String path) throws UnknownHostException {
        return new Greeting(String.format(template, path, InetAddress.getLocalHost().getHostName()));
    }
}
