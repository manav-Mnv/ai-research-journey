# AI Research Journey

A public log of my path into AI research: setup, learning, experiments and notes, one phase at a time.

## Current phase

**Phase 0: Setup & Commit** (Oct 10 to Oct 24, 2026)

- [x] Check my ZenBook's chip (Intel or AMD): **Intel Core Ultra 5 225H**
- [ ] Install Python, VS Code, Git
- [x] Create GitHub repo `ai-research-journey`
- [ ] Install PyTorch (XPU build if Intel); run one matrix multiply
- [ ] Create a Kaggle account, verify phone, run one GPU notebook
- [ ] Watch 3Blue1Brown "Neural Networks", chapters 1 to 4
- [ ] Fix a daily slot: minimum 2 hours, same time every day
- [ ] Decide on SRFP 2027 (deadline Nov 30, 2026)

## Setup notes

| Item | Value |
| --- | --- |
| Laptop | ASUS ZenBook |
| CPU | Intel Core Ultra 5 225H (14 cores) |
| GPU | Intel Arc 130T (integrated, shares system RAM), driver 32.0.101.8132 |
| NPU | Intel AI Boost |
| RAM | 16 GB LPDDR5 |
| Disk | 1 TB NVMe SSD |
| PyTorch backend | `xpu` (Intel GPU) |
| Python | 3.11 (venv `ai`) |
| PyTorch | 2.14.1+xpu |
| Daily slot | _TBD_ |

## Repo layout (planned)

```
phase-0-setup/     setup scripts and the first matrix-multiply test
notes/             notes from videos, papers and courses
log.md             daily log: date, hours, what I did, what's next
```

## Log

| Date | Hours | What I did |
| --- | --- | --- |
| 2026-10-13 | | Created this repo, checked chip (Intel Core Ultra 5 225H) |
