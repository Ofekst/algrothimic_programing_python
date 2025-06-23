import math


def calculate_euclidean_distance(p1, p2):
    """
    Calculates the Euclidean distance between two points in 2D space.

    :param p1: The first point
    :param p2: The second point
    :return: The Euclidean distance between p1 and p2 as float
    """
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def find_closest_point(current_point, points, visited):
    """
    Finds the closest unvisited point in the list of points.
    :param current_point: The point from which distances are calculated
    :param points: List of all points
    :param visited: Set of indices of already visited points
    :return: The closest unvisited point and its index
    """
    min_distance = float("inf")
    closest_point = None
    closest_index = -1

    for i, point in enumerate(points):
        if i not in visited:
            distance = calculate_euclidean_distance(current_point, point)
            if distance < min_distance:
                min_distance = distance
                closest_point = point
                closest_index = i

    return closest_point, closest_index

def solve(points):

    visited_points = set()
    best_path = [points[0]]
    visited_points.add(0)

    current_point = points[0]

    while len(visited_points) < len(points):
        closest_point, closest_index = find_closest_point(current_point, points, visited_points)
        if closest_point:
            best_path.append(closest_point)
            visited_points.add(closest_index)
            current_point = closest_point

    best_path.append(points[0])

    return best_path