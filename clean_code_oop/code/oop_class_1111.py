class Employee:
    # 建構式
    def __init__(self, job_title, job_desc, job_inds):
        self.job_title = job_title 
        self.job_desc = job_desc 
        self.job_inds = job_inds 
    # 方法(Method)
    def print_job(self):
        print(f"這個工作職稱是{self.job_title} 工作描述是{self.job_desc}")


employee = Employee(job_title = '資訊工程師', job_desc = '寫程式', job_inds = '軟體業')
employee.print_job()


