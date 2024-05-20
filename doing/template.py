"""
新闻类模板
"""
import os

print("This script is template.")
exit(0)


class TEMPLATE():
    name = ""

    def __init__(self, token):
        self.token = token

    def receice(self):
        print("template")

    def main(self):
        print("template")


if __name__ == '__main__':
    env_name = 'template'
    token = os.getenv(env_name)
    if not token:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)
    TEMPLATE(token).main()
