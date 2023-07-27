from django import template
from django.http import HttpResponse
register = template.Library()

def get_TotalProjects(test):

    return test

register.filter('TotalProjects', get_TotalProjects)

def get_TotalTasks(test):

    return test

register.filter('TotalTasks', get_TotalTasks)

def get_TotalPayments(test):

    return test

register.filter('TotalPayments', get_TotalPayments)


def get_completedProjects(test):

    return test

register.filter('completedProjects', get_completedProjects)

def get_completedTasks(test):

    return test

register.filter('completedTasks', get_completedTasks)

def get_completedPayments(test):

    return test

register.filter('completedPayments', get_completedPayments)


def get_incompleteProjects(test):

    return test

register.filter('incompleteProjects', get_incompleteProjects)

def get_incompleteTasks(test):

    return test

register.filter('incompleteTasks', get_incompleteTasks)

def get_incompletePayments(test):

    return test

register.filter('incompletePayments', get_incompletePayments)