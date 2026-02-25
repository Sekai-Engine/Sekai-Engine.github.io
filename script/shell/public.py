import sys
import shell.private as private

def options(version):
    long_options = [
        private.CmdOption(
            abbr='-h',
            full='-help',
            vari='',
            defa='',
            desc='显示编码的基本信息并退出.'
        ),
        private.CmdOption(
            abbr='-v',
            full='--version',
            vari='',
            defa='',
            desc='显示版本号并退出.'
        ),
        private.CmdOption(
            abbr='-s',
            full='--status',
            vari='(build/debug)',
            defa='build',
            desc='wiki构建状态.'
        ),
        private.CmdOption(
            abbr='-p',
            full='--port',
            vari='[int]',
            defa='9999',
            desc='设置调试使用的端口.'
        ),
    ]
    args = sys.argv.copy()
    if long_options[0].set_options(args):
        private.help_message(long_options, version)
        sys.exit(1)
    
    if long_options[1].set_options(args):
        print(f"Sekai Wiki {version}")
        sys.exit(1)

    result_shell = {}
    print(long_options[2].options(args))
    result_shell["status"] = long_options[2].options(args),
    result_shell["port"] = int(long_options[3].options(args)),

    return result_shell
    




