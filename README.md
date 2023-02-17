迁移到 [Memo](https://github.com/usememos/memos) 用了一段时间，体验挺好。写了一个简单的 [Python 脚本 - PostMemos]( https://github.com/Domonlee/postMemos ) 。通过 `request` 去给 `OpenApi` 发送请求。并用别名的方式去调用这个脚本，实现了命令行快速发送 Memo。

```python
OPENAPI = 'input your OpenApi'
...
post = get_args() 
data = requests.post(OPENAPI, headers=HEADER, data=post.encode('utf-8'))
```

利用 `argparse` 增加了参数 `-t（标签） 和 -v （可见度）`，可不用输入，默认情况下标签是 `#inbox`，内容是 `仅自己可见`。

```python
parser = argparse.ArgumentParser(description='命令行快速发送Memo')
parser.add_argument("c", type=str, help="内容参数，默认不用输入")
parser.add_argument("--T", '-t', default="#inbox", type=str, help="标签参数，默认为#inbox标签")
parser.add_argument("--V", '-v', default="PRIVATE", type=str, help="公开范围，默认为PRIVATE，还可选择PUBLIC，PROTECTED")

args = parser.parse_args()
...    
```


在终端的配置，例如我使用 `zsh`，它默认的配置在 `~/.zshrc`。在其中增加下面的别名

```bash
alias memo="/usr/bin/python3 /yourlocation/postMemos/main.py"
```

修改之后别忘记 `source ~/.zshrc` 更新一下配置，便可以方便的在终端，或者 IDE 里快速的发送 Memo 了。

![send_memo_use_terminal](https://user-images.githubusercontent.com/3839583/219588976-247a6556-d0e8-4242-89e7-cb57d8adb342.jpg)
![send_memo_use_terminal_result](https://user-images.githubusercontent.com/3839583/219588964-50907702-614d-4b6e-aa08-eabf7ba17764.jpg)

