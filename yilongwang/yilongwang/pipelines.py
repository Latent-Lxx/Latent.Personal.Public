
from yilongwang import publicMians as pm;
from yilongwang.items import Yilongwang_List_Item;
from yilongwang.items import Yilongwang_Comment_Item;

class YilongwangPipeline(object):

    def process_item(self, item, spider):
        if  isinstance(item, Yilongwang_List_Item):
            # 只存到ID后面的取出来再加
            hotelUrls = 'http://hotel.elong.com/ajax/comment/getcommentbypage/?hotelId={id}'.format(id=item['projectId'])
            with open('/home/latent-lxx/Desktop/elong/hotelUrls','a+') as w :
                w.write(hotelUrls);
                w.write('\n');
            pm.getPrint('==> 写入成功！','',32);
            return item

        elif isinstance(item, Yilongwang_Comment_Item):

            data = item['comment'];
            name = item['name'];
            pm.getPrint(data, '', 32);

            with open('/home/latent-lxx/Desktop/elong/comment_data/{file_name}'.format(file_name=name),'a+') as w :
                w.write(data);
                w.write('\n');
                pm.getPrint('==> 写入成功！', '', 32);
                return item

        else:
                pm.getPrint('==> 写入失败,请检查配置!','',31);

