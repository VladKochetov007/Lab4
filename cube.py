from turtle import *
import math
import time
import numpy as np

def rotate_points(points, rotation_matrix):
    return [np.array(rotation_matrix) @ np.array(point) for point in points]

def get_rotation_matrix_x(angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [
        [1, 0, 0],
        [0, cos_a, -sin_a],
        [0, sin_a, cos_a]
    ]

def get_rotation_matrix_y(angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [
        [cos_a, 0, sin_a],
        [0, 1, 0],
        [-sin_a, 0, cos_a]
    ]

def get_rotation_matrix_z(angle):
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return [
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ]

class Cube:
    def __init__(self, size=100):
        self.vertices = [
            [-size/2, -size/2, -size/2],
            [size/2, -size/2, -size/2],
            [size/2, size/2, -size/2],
            [-size/2, size/2, -size/2],
            [-size/2, -size/2, size/2],
            [size/2, -size/2, size/2],
            [size/2, size/2, size/2],
            [-size/2, size/2, size/2]
        ]
        
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def rotate_x(self, angle):
        self.angle_x += angle
        rotation_matrix = get_rotation_matrix_x(angle)
        self.vertices = rotate_points(self.vertices, rotation_matrix)

    def rotate_y(self, angle):
        self.angle_y += angle
        rotation_matrix = get_rotation_matrix_y(angle)
        self.vertices = rotate_points(self.vertices, rotation_matrix)

    def rotate_z(self, angle):
        self.angle_z += angle
        rotation_matrix = get_rotation_matrix_z(angle)
        self.vertices = rotate_points(self.vertices, rotation_matrix)

    def project(self, distance=300):
        projected_vertices = []
        for vertex in self.vertices:
            x, y, z = vertex
            factor = distance / (distance + z)
            projected_x = x * factor
            projected_y = y * factor
            projected_vertices.append((projected_x, projected_y))
        return projected_vertices

    def draw(self, t, distance=300):
        t.clear()
        projected = self.project(distance)
        
        for edge in self.edges:
            start, end = edge
            t.penup()
            t.goto(projected[start])
            t.pendown()
            t.goto(projected[end])

screen = Screen()
screen.setup(800, 600)
screen.title("3D Cube Projection")

t = Turtle()
t.speed(0)
t.hideturtle()

cube = Cube(150)

screen.tracer(0)

try:
    while True:
        cube.rotate_x(0.02)
        cube.rotate_y(0.03)
        cube.rotate_z(0.01)
        cube.draw(t)
        screen.update()
        time.sleep(0.01)
except KeyboardInterrupt:
    pass

screen.bye()

