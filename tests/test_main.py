def test_compare_products():
    local_products = [
        {"id": 1, "title": "Laptop"},
        {"id": 2, "title": "Mouse"}
    ]

    api_products = [
        {"id": 3, "title": "Laptop"},
        {"id": 4, "title": "Keyboard"}
    ]

    local_names = {product["title"] for product in local_products}
    api_names = {product["title"] for product in api_products}

    common = local_names & api_names
    only_local = local_names - api_names
    only_api = api_names - local_names

    assert common == {"Laptop"}
    assert only_local == {"Mouse"}
    assert only_api == {"Keyboard"}



def test_no_matching_products():
    local_products = [
        {"id": 1, "title": "Laptop"}
    ]

    api_products = [
        {"id": 2, "title": "Phone"}
    ]

    local_names = {product["title"] for product in local_products}
    api_names = {product["title"] for product in api_products}

    common = local_names & api_names

    assert common == set()    



def test_all_products_match():
    local_products = [
        {"id": 1, "title": "Laptop"},
        {"id": 2, "title": "Mouse"}
    ]

    api_products = [
        {"id": 10, "title": "Laptop"},
        {"id": 20, "title": "Mouse"}
    ]

    local_names = {product["title"] for product in local_products}
    api_names = {product["title"] for product in api_products}

    common = local_names & api_names
    only_local = local_names - api_names
    only_api = api_names - local_names

    assert common == {"Laptop", "Mouse"}
    assert only_local == set()
    assert only_api == set()    