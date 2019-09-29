import pytest

@pytest.fixture
def structured_contract_data():
    contract = """<document> 
        <section title="Parties">
                <clause>This contract binds Alice Smith and Bob Turner as follows:</clause>
            </section>
            <section title="Terms">
                <clause>This contract is effective from the date that it is signed.</clause>
                <clause>This contract is valid in the United Kingdom.</clause>
                <clause>This contract expires three years after the date that it is signed.</clause>
            </section>
        </document>
    """
    return contract