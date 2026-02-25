class CmdOption:
    def __init__(self, abbr = '', full = '', vari = '', defa = '', desc = ''):
        self.abbr = abbr      # 短选项，如 '-h'
        self.full = full      # 长选项，如 '--help'
        self.vari = vari      # 参数类型，如 '[int]'
        self.defa = defa      # 默认值
        self.desc = desc      # 描述信息
    
    # 获取选项值
    def options(self, args):
        for i, arg in enumerate(args):
            if arg == self.abbr or arg == self.full:
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    return args[i + 1]
        return self.defa

    # 检查是否设置
    def set_options(self, args):
        return self.abbr in args or self.full in args

def help_message(long_options, version):
    data = ''
    data += f'Sekai Wiki {version}'
    data += '\nOptions:'
    print(data)
    for v in long_options:
        data = f' {v.abbr}, {v.full} {v.vari}'
        data_len = len(data)
        # 计算需要添加的制表符数量
        tabs_needed = max(1, 3 - (data_len // 8))
        data += '\t' * tabs_needed
        data += f'{v.desc}'
        print(data)



