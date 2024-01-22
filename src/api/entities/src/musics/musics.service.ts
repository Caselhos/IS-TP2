import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class MusicsService {
    private prisma = new PrismaClient();

    async findAll(): Promise<any[]> {
        return this.prisma.musics.findMany();
    }
    findOne(id: string) {
    return this.prisma.musics.findUnique({ where: { id } });
  }

  create(data: any) {
    return this.prisma.musics.create({ data });
  }

  update(id: string, data: any) {
    return this.prisma.musics.update({ where: { id }, data });
  }

  remove(id: string) {
    return this.prisma.musics.delete({ where: { id } });
  }
  getArtists(id: string) {
    return this.prisma.musics.findUnique({ where: { id } }).artists_musics();
  }

  getAlbum(id: string) {
    return this.prisma.musics.findUnique({ where: { id } }).albums();
  }
}
