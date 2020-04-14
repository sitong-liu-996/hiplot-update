import os
import time
from pathlib import Path
from test_e2e import create_browser_chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_jupyter_notebook() -> None:
    token = os.environ["NOTEBOOK_TOKEN"]
    artifacts_path = Path(__file__).parent / ".." / "artifacts"
    artifacts_path.mkdir(exist_ok=True, parents=False)

    driver = create_browser_chrome()
    num_err = 0
    try:
        driver.get(f"http://localhost:8888/notebooks/test_notebook.ipynb?token={token}")
        time.sleep(2)
        driver.save_screenshot(str(artifacts_path / "step1.png"))

        print('Logs before execution:')
        for l in driver.get_log('browser'):
            print(f'    {str(l)}')

        # Find the "Run" button
        run_btn = driver.find_element_by_css_selector("#run_int > button[title='Run']")
        run_btn.click()
        driver.save_screenshot(str(artifacts_path / "step2.png"))

        time.sleep(5)
        driver.save_screenshot(str(artifacts_path / "step3.png"))
        print('Logs after execution:')
        for l in driver.get_log('browser'):
            print(f'    {str(l)}')
            if l['level'] != 'INFO':
                num_err += 1
    finally:
        driver.quit()
    assert num_err == 0