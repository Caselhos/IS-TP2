import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class ArtistsService {
    private prisma = new PrismaClient();

    async findAll(): Promise<any[]> {
        return this.prisma.artists.findMany();
    }
    findOne(id: string) {
    return this.prisma.artists.findUnique({ where: { id } });
  }

  create(data: any) {
    return this.prisma.artists.create({ data });
  }

  update(id: string, data: any) {
    return this.prisma.artists.update({ where: { id }, data });
  }

  remove(id: string) {
    return this.prisma.artists.delete({ where: { id } });
  }
  getMusics(id: string) {
    return this.prisma.artists.findUnique({ where: { id } }).artists_musics();
  }
}
