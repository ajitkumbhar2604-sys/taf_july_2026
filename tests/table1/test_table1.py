def test_count_1(read_data):
    source, target = read_data
    source.show()
    print(source.schema.json())
    target.show()
    assert True