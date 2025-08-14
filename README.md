# CyberShield
## 项目运行截图

### 网络流量监控
![Traffic Monitor](docs/exports/traffic_monitor_demo.png)

### 钓鱼网址检测
![Phishing Check](docs/exports/phishing_check_demo.png)

### 弱口令审计
![Password Audit](docs/exports/password_audit_demo.png)

## 样例数据
- [Traffic Monitor CSV](docs/exports/traffic_log_sample.csv)
- [Phishing Check CSV](docs/exports/phishing_check_sample.csv)
- [Password Audit CSV](docs/exports/password_audit_sample.csv)


一个适合高中生独立开发的网络安全可视化工具，包含：
- 网络流量监控（模拟模式）
- 钓鱼网址检测
- 弱口令审计

运行方式：
```bash
pip install -r requirements.txt
streamlit run app.py

---

## 8️⃣ docs/demo_script.md

新建 `docs/demo_script.md`（面试演示用）：

```markdown
## CyberShield Student Edition 演示脚本

1. 打开 Traffic Monitor，展示流量表格和图表
2. 切换到 Phishing Check，输入几个可疑网址，检测结果
3. 切换到 Weak Password Audit，输入一些密码，展示强度结果
