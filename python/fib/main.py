from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from typing import List


def _get_fib_number(n: int, sequence: List[int]) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequence[n-1] + sequence[n-2]


def fibonacci(n: int) -> List[int]:
    """Return the first `n` Fibonacci numbers."""
    if n < 0:
        raise Exception("This can only take positive integers")
    fib_list = []
    for i in range(n):
        result = _get_fib_number(i, fib_list)
        fib_list.append(result)
    return fib_list


class GetFibs(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)

        if "n" not in params:
            self.send_response(422)
            return

        try:
            key = int(params["n"][0])
        except (IndexError, ValueError):
            self.send_response(422)

        nums = fibonacci(key)

        # convert nums from int to string list
        str_nums = [str(n) for n in nums]
        final_nums = ", ".join(str_nums)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(final_nums, "UTF-8"))
        return


if __name__ == "__main__":
    from http.server import HTTPServer

    httpd = HTTPServer(("", 8000), GetFibs)
    httpd.serve_forever()
