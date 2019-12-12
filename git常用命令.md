# git 常用命令和设置安装

## git 设置

> 在 `cd ~/.ssh` 目录下生成 `ssh` 密钥

    ssh-keygen

> 提交时转换为 LF，检出时不转换

    git config --global core.autocrlf input

> 拒绝提交包含混合换行符的文

    git config --global core.safecrlf true

> 设置用户名

    git config --global user.name <你的名字>

> 设置邮箱

    git config --global user.email <xxx@xxx.com>

> 查看用户名

    git config user.name

> 查看邮箱

    git config user.email 查看邮箱

> 设置 git 记住密码

    git config --global credential.helper store

> 查看 git 设置

    git config --list

## git 常用命令

```bash shell
#将目录变成仓库
git init

#添加文件到 git 仓库
git add <filename>

#查看未提交
git status

#暂存所有更改
git add .

#提交当前所有暂存
git commit –m <注释说明>

#克隆仓库
git clone <仓库地址>

#切换分支
git checkout <分支名>

#合并分支
git merge <分支名>

#查看分支所有分支包括远程分支
git branch -a

#放弃所有更改和远端保持一致
git fetch --all
git reset --hard origin/master

#回退版本
git reset HEAD^  回退到上个版本
git reset --hard HEAD~3  回退到前3次提交之前，以此类推，回退到n次提交之前
git reset --hard commit_id

#新建分支
git checkout -b <name>

```
