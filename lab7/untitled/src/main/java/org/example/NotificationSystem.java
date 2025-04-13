package org.example;

import org.example.Observer;
import org.example.Subject;

import java.util.ArrayList;
import java.util.List;

class NotificationSystem implements Subject {
    private List<Observer> observers;

    public NotificationSystem() {
        observers = new ArrayList<>();
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(String message) {
        for (Observer observer : observers) {
            observer.update(message);
        }
    }
}
