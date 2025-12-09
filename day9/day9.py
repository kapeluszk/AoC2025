with open("/home/kapelusz/PycharmProjects/AoC2025/day9/input.txt") as f:
    lines = f.read().splitlines()



points = [list(map(int, line.split(","))) for line in lines]

def rectangle_area(p1, p2) -> int:
    length = abs(p1[0] - p2[0]) + 1
    width = abs(p1[1] - p2[1]) + 1
    return length * width

def part1(points) -> int:
    max_area = 0
    for p in points:
        for q in points:
            if p != q:
                area = rectangle_area(p, q)
                if area > max_area:
                    max_area = area
    return max_area

def normalize_edge(p1,p2) -> list:
    if p1[0] == p2[0]:
        return ["V", p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])]
    else:
        return ["H", p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])]

def prepare_edges(points) -> list:
    edges = []
    n = len(points)
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edge = normalize_edge(p1, p2)
        edges.append(edge)
    return edges

def is_rectangle_valid(p1, p2, edges) -> bool:
    rect_x1 = min(p1[0], p2[0])
    rect_x2 = max(p1[0], p2[0])

    rect_y1 = min(p1[1], p2[1])
    rect_y2 = max(p1[1], p2[1])
    for edge in edges:
        if edge[0] == "V":
            x = edge[1]
            y1 = edge[2]
            y2 = edge[3]
            if rect_x1 < x < rect_x2:
                overlap_start = max(rect_y1, y1)
                overlap_end = min(rect_y2, y2)
                if overlap_start < overlap_end:
                    return False
        else:
            y = edge[1]
            x1 = edge[2]
            x2 = edge[3]
            if rect_y1 < y < rect_y2:
                overlap_start = max(rect_x1, x1)
                overlap_end = min(rect_x2, x2)
                if overlap_start < overlap_end:
                    return False
    return True

def ray_casting(point, edges) -> int:
    x, y = point
    intersections = 0
    for edge in edges:
        if edge[0] == "V":
            edge_x = edge[1]
            edge_y1 = edge[2]
            edge_y2 = edge[3]
            if edge_x > x and edge_y1 <= y <= edge_y2:
                intersections += 1
    return intersections

def part2(points) -> int:
    edges = prepare_edges(points)
    max_area = 0
    for p in points:
        for q in points:
            if p != q:
                if is_rectangle_valid(p, q, edges):
                    center = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2]
                    if ray_casting(center, edges) % 2 != 0:
                        area = rectangle_area(p, q)
                        if area > max_area:
                            max_area = area
    return max_area


print(part1(points))
print(part2(points))