# -*- coding: utf-8 -*- 
import requests
import argparse

#填入Memos后台获取的OpenAPI
OPENAPI = ''
HEADER = { 'Content-Type': 'application/json' }

def get_args():
    parser = argparse.ArgumentParser(description='命令行快速发送Memo')
    parser.add_argument("c", type=str, help="内容参数，默认不用输入")
    parser.add_argument("--T", '-t', default="inbox", type=str, help="标签参数，默认为#inbox标签")
    parser.add_argument("--V", '-v', default="PRIVATE", type=str, help="公开范围，默认为PRIVATE，还可选择PUBLIC，PROTECTED")

    args = parser.parse_args()
    #增加回车换行，填入tag
    content = args.c + '\\r\\n#' + args.T
    post = '{"content":"' +content + '","visibility":"'+args.V+'"}'

    return post

def memos():
    post = get_args() 
    data = requests.post(OPENAPI, headers=HEADER, data=post.encode('utf-8'))
    data.raise_for_status()

if __name__ == "__main__":
    memos()
