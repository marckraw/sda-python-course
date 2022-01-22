# 12.01.2022 - Saturday - Testowanie oprogramowania i TDC


## Przydatne linki
- 

## Przydatne z z tego dnia
- cmd + shift (ctrl + shift in windows) + strzalki w dol i w gore - przesuwanie aktualnie zaznaczonej linijki w dol i gore
- Fixtures
  - Test Fixture
    - setup_method() - wykonywana przed kazdym testem
    - teardown_method() - wykonywana bezposrednio po wykonaniu kazdej metodytestowej, nawet w przypadku wystapienia bledu. Jednakze, jezeli podcxzas wykonywania metody setup_method() zostanie zgloszony wyjatek, wtedy metoda teardown_method() nie jest wykonywana
  - Parametrized tests
  ```
  class TestSample:

    @pytest.mark.parametrize('value,expected', [
        [1, 1],
        [2, 2]
    ])
    def test_multiple_values(self, value, expected):
        assert value == expected
  ```

## Przydatne moduly
```python

```
