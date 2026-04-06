# SauceDemo UI Tests

Учебный проект с UI-автотестами на Python + pytest + Playwright.

## Покрытие
- открытие страницы логина
- успешный логин
- добавление товара в корзину
- проверка товара в корзине
- переход к первому шагу checkout

## Стек
- Python
- pytest
- Playwright

## Запуск
```bash
pip install -r requirements.txt
python -m playwright install chromium
pytest --headed