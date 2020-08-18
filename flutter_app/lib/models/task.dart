import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

class Task {
  int id;
  String title;
  String description;
  bool completed;

  Task({this.id, @required this.title,this.description, this.completed = false});

  void toggleCompleted() {
    completed = !completed;
  }

  factory Task.fromJason(Map<String, dynamic> json) {
    return Task(
      id: json['id'],
      title: json['Title'],
      description:json['Description'],
      completed: json['completed'],
    );
  }
  dynamic toJson() => { 'Title': Title, 'completed': completed };
}