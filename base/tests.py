def convert_excel(request):
    wb = openpyxl.Workbook() 
    sheet = wb.active 
    data = EventsForm.objects.all()
    title = ["updated_date","title","Name","Email","company","event","linkedin","website"]
    for i,x in enumerate(title):
        cell_obj = sheet.cell(row = 1, column = i+1)
        cell_obj.value = x
    filepath = "sample5.xlsx"
    for i,x in enumerate(data,2):
        row_data = [x.updated_date,x.title,x.Name,x.Email,x.company,x.event,x.linkedin,x.website]
        for j,y in enumerate(row_data):
            cell_obj = sheet.cell(row = i+1, column = j+1)
            cell_obj.value = y
            print(i,j)
    wb.save(filepath) 
    filename = 'Datas.xlsx'
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response