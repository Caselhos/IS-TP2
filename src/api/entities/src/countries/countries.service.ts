import { Injectable } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class CountriesService {
    private prisma = new PrismaClient();

    async findAll(): Promise<any[]> {
        return this.prisma.countries.findMany();
    }
    findOne(id: string) {
    return this.prisma.countries.findUnique({ where: { id } });
  }

  create(data: any) {
    return this.prisma.countries.create({ data });
  }

  update(id: string, data: any) {
    return this.prisma.countries.update({ where: { id }, data });
  }

  remove(id: string) {
    return this.prisma.countries.delete({ where: { id } });
  }
}
