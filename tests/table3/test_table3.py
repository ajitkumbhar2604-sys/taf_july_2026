from src.data_validations.count_validation import count_check
from src.data_validations.records_only_source import record_only_source
from src.data_validations.records_only_target import record_only_target
from src.data_validations.duplicate_validation import duplicate_check
from src.data_validations.uniqueness_validation import uniqueness_check
from src.data_validations.not_null_validation import null_value_check
from src.data_validations.data_compare_validation import data_compare
from src.data_validations.schema_validation import schema_check


def test_count(read_data):
    source, target = read_data
    source.show()
    target.show()
    status  = count_check(source, target)
    assert status == 'PASS'

def test_records_only_source(read_data, read_config):
    source, target = read_data
    config,_ = read_config
    key_columns = config['validation_config']['key_columns']
    num_records = config['validation_config']['num_records']
    status = record_only_source(source, target, key_columns, num_records=num_records)

    assert status == 'PASS'

def test_records_only_target(read_data, read_config):
    source, target = read_data
    config,_ = read_config
    key_columns = config['validation_config']['key_columns']
    num_records = config['validation_config']['num_records']
    status = record_only_target(source, target, key_columns, num_records=num_records)

    assert status == 'PASS'

def test_duplicate(read_data, read_config):
    _, target = read_data
    config,_ = read_config
    key_columns = config['validation_config']['key_columns']
    num_records = config['validation_config']['num_records']
    status = duplicate_check( target, key_columns, num_records=num_records)

    assert status == 'PASS'

def test_uniqueness_check(read_data,read_config):
    _, target_df = read_data
    config,_ = read_config
    unique_columns = config['validation_config']['unique_cols']
    status = uniqueness_check(df= target_df,unique_cols=unique_columns)
    assert status == 'PASS'

def test_not_null_check(read_data,read_config):
    _, target_df = read_data
    config,_ = read_config
    not_null_columns = config['validation_config']['unique_cols']
    num_records = config['validation_config']['num_records']
    status = null_value_check(df= target_df,not_null_columns=not_null_columns,failed_records=num_records)
    assert status == 'PASS'


def test_schema_check(read_data, read_config):
    source, target = read_data
    config,_ = read_config
    status = schema_check( source, target)
    assert status == 'PASS'

def test_data_compare(read_data, read_config):
    source, target = read_data
    config,_ = read_config
    key_columns = config['validation_config']['key_columns']
    num_records = config['validation_config']['num_records']
    status = data_compare(source_df=source, target_df=target, key_columns = key_columns, num_records=num_records)

    assert status == 'PASS'