# DevSecOps Demo

Простой проект, демонстрирующий полностью автоматический DevSecOps-пайплайн, который защищает код от утечек секретов, уязвимых зависимостей и опасных паттернов кода.

## Инструменты безопасности

- **Gitleaks** — поиск закоммиченных паролей, токенов, ключей.
- **Trivy** — сканирование зависимостей и Docker-образов на известные CVE.
- **Semgrep** — статический анализ кода по правилам OWASP Top 10.

## CI/CD (GitHub Actions)

Пайплайн `.github/workflows/devsecops.yml` запускается при каждом push в `main` и при Pull Request. При обнаружении проблем билд падает и уведомления отправляются в Slack и Telegram.

### Требуемые секреты GitHub

- `SLACK_WEBHOOK_URL` — вебхук для оповещений в Slack.
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` — для уведомлений в Telegram.
- `SEMGREP_APP_TOKEN` — для интеграции с дашбордом Semgrep (опционально).

## Блокировка мёржа

Настройте защиту ветки `main`:
1. Settings → Branches → Add rule.
2. Включите **Require status checks to pass before merging**.
3. Добавьте чеки: `Gitleaks - поиск секретов`, `Trivy - сканирование уязвимостей`, `Semgrep - статический анализ кода`.

Теперь опасный код нельзя будет слить, пока все проверки не пройдут.

## Локальная проверка (pre-commit)

Установите pre-commit и хуки:
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
