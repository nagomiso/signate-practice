# coding: utf-8
import re


SUBJECT_REGEX = re.compile(r'^Subject: ')
FORWARD_HEAD_REGEX = re.compile(r'^(?:-\s?)+forwarded by')
QUOTE_REGEX = re.compile('(?:-\s)+original message(?:\s-)+$')
ATTACHMENT_REGEX = re.compile(r'^-\s(?:[a-zA-Z0-9_]+\s)*\.\s([a-zA-Z0-9]+)')


def parse(document_lines):
    # 件名抽出
    subject = SUBJECT_REGEX.sub('', document_lines.pop(0))
    if 0 < len(document_lines):
        tail_line = document_lines.pop()
        # 添付ファイルの拡張子抽出
        attachment_match = ATTACHMENT_REGEX.match(tail_line)
        if attachment_match:
            attachment_ext = attachment_match.groups()[0]
        else:
            attachment_ext = 'no attachment'
            document_lines.append(tail_line)
    else:
        attachment_ext = 'no attachment'
    body = ''
    # 本文抽出
    for line in document_lines:
        body += line
    return {
        'subject': subject,
        'subject_length': len(subject.split()),
        'body': body,
        'body_length': len(body.split()),
        'attachment_ext': attachment_ext,
    }


if __name__ == '__main__':
    with open('./train2/train_0250.txt') as f:
        print(parse(f.readlines()))
    with open('./train2/train_1017.txt') as f:
        print(parse(f.readlines()))
