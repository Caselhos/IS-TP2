import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class AlbumsService {
    private prisma = new PrismaClient();

    async findAll(): Promise<any[]> {
        return this.prisma.albums.findMany();
    }
    findOne(id: string) {
    return this.prisma.albums.findUnique({ where: { id } });
  }

  create(data: any) {
    return this.prisma.albums.create({ data });
  }

  update(id: string, data: any) {
    return this.prisma.albums.update({ where: { id }, data });
  }

  remove(id: string) {
    return this.prisma.albums.delete({ where: { id } });
  }
}
