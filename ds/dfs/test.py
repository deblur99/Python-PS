from graph_generator import generate_test_case
from graph_parser import parse_graph


if __name__ == "__main__":
    generate_test_case(v_count=8)
    print(parse_graph())